import praw
import pandas as pd
import re
import string
from datetime import datetime


#!which python
reddit = praw.Reddit('irbot_readonly')


def contains_update_text(post):
    #result = re.search('UPDATE', post.title[:100], re.IGNORECASE)
   # if result:
    if 'update' in post.title.lower():
        return True
    return False

def extract_title(post):
    #title = re.sub('\(..[0-9]*..\)', '', post.title) # remove the (age, gender) inzz
    title = re.sub('\(.+?\)', '', post.title) # remove the (age, gender) inzz
    return '\t ' + title

def extract_tldr(post):
    tldr = ''
    # Result will include punctuation!
    txt = post.selftext
    result = re.search('TL[;:,\s]*DR[;:,*]*', txt, re.IGNORECASE)
    if result:
        tldr = txt.split(result.group())[-1].strip()
    else:
        result2 = re.search('TD[;:,\s]*LR[;:,*]*', txt, re.IGNORECASE)
        if result2:
            tldr = txt.split(result2.group())[-1].strip()
        else: # found NEITHR tldr NOR tdlr
            print(f'-' * 40)
            print(f'\t \t \t !! ERROR in extract_tldr !!! No tldr found in post {post.url} with text {txt}')
            print(f'-' * 40)
    return '\t' + tldr.split('\n')[0]

def extract_two_nested_replies(post, idx=0):
    reply = ''
    reply_to_reply = ''

    try:
        text = post.comments[idx].body
        reply = text.split('.')[0] # only take first sentence for now. also fails on er. etc.

        text = post.comments[idx].replies[0].body 
        reply_to_reply = text.split('.')[0]
    except Exception as e:
        print(f'\t \t \t  Exception extracting {idx}-th replies for {post}: {e}')
        pass

    return reply, reply_to_reply


def scrape_reddit(limit=5):
    all_dialogs = []
    #for submission in reddit.subreddit('relationships').top('year', limit=limit):
    
    for i, submission in enumerate(reddit.subreddit('relationships').hot(limit=limit)):
        now = str(datetime.now())[5:19]
        print(f'[{i}/{limit} ({now})] {submission.title} - {submission.url} ')

        if not contains_update_text(submission):
            tldr = extract_tldr(submission)
            txt, txt2 = extract_two_nested_replies(submission, idx=0)
            title = extract_title(submission)
            txt3, txt4 = extract_two_nested_replies(submission, idx=1)
            print('title', title)
            all_dialogs.extend([tldr, txt, txt2, title, txt3, txt4])

        if i%50 == 0:
            print('-' * 50)

    return all_dialogs

def main():
    start = str(datetime.now())[5:19]
    dialogs = scrape_reddit(limit=200)
    print(len(dialogs))
    df = pd.DataFrame(dialogs)
    print(df.head())
    df.to_csv('./csv/scrape_hot_200_tldrfix.csv')
    end_time = str(datetime.now())[5:19]
    print(f'Start time: {start}, endtime: {end_time}')

#def clean_text(sentence):
#    return re.findall("[\w']+", sentence)

if __name__ == '__main__':
    main()
