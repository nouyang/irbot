# irbot

inadvisable relationship bot, updated

Last version created just as GPT was coming out. Results not great. Let's
redo this now with GPT.

# Context 

SIGTBD joke conference.

SIGBD2019

IRBot: InadvisableRelationshipBot

Many graduate students struggle to deal emotionally with daily life stresses, ranging from overdue problem sets to not dying at sea. Additionally, computer scientists may feel more comfortable typing at a screen than engaging in human contact. Although therapy chatbots exist and in fact have reached millions of smartphone users, they run on remote servers, creating privacy concerns. In this work, we propose that a local chatbot can also provide useful advice and can reach the vulnerable sub-population of computer science grad students. We create InadvisableRelationshipBot (IRBot) using high-quality online commentary from www.reddit.com/r/relationships.


# Related links
`irbot_test.py`

https://gist.github.com/dredwardhyde/8419b8adc130075ba82ffe75bbe0a819

https://medium.com/geekculture/fine-tune-eleutherai-gpt-neo-to-generate-netflix-movie-descriptions-in-only-47-lines-of-code-40c9b4c32475

# Notes

Dell xps15, nvidia gtx1050, 4 gb memory

Had a lot of issues. Solution at
https://askubuntu.com/questions/1077061/how-do-i-install-nvidia-and-cuda-drivers-into-ubuntu.
https://askubuntu.com/a/1288405/67349

Basically, remove all cuda/nvidia packages. Install nvidia-driver-495, then
CUDA 11.5.0, then libcudnn8, and reboot.

```
sudo apt install nvidia-driver-495
wget https://developer.download.nvidia.com/compute/cuda/11.5.0/local_installers/cuda_11.5.0_495.29.05_linux.run
sudo sh ./cuda_11.5.0_495.29.05_linux.run

Click ACCEPT EULA and then **UNSELECT** the video driver (don't install
over the nvidia-driver-495 we just installed

```

```
/etc/profile.d/cuda.sh
# set PATH for cuda 11.5 installation
if [ -d "/usr/local/cuda-11.5/bin/" ]; then
    export PATH=/usr/local/cuda-11.5/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda-11.5/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
fi
```

```
echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda_learn.list
sudo apt-key adv --fetch-keys  http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt update
sudo apt install libcudnn8
reboot
```

Then check installed
```
~$ nvidia-smi
~$ nvcc -V
~$ sbin/ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn
```


### example errors

- NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
- Could not use `sudo ubuntu-drivers autoinstall` (got E: Unable to correct problems, you have held broken packages.)



# Example output

medium: DialoGPT 345M model
dialogpt-large: DialoGPT 762M model
Samll: DialoGPT 117M model

```
>> User:Hi
DialoGPT: Hiya
>> User:Bye
DialoGPT: Bye bye
>> User:Does money buy happiness?
DialoGPT: No, but it does buy a new car.
>> User:What is the best way to buy happiness ?
DialoGPT: I don't know, but I know the best way to buy happiness is to buy a new car.
>> User:This is so difficult !
DialoGPT: I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I know, I
```

# Notes 

json file tells you model name

```
Update 2021-03-11: The cache location has now changed, and is located in ~/.cache/huggingface/transformers, as it is also detailed in the answer by @victorx.
```

# using colab

https://theaidigest.in/conversational-response-generation-using-dialogpt/

# dialogpt


>> User:Hello there
DialoGPT: General Kenobi
>> User:Who is general kenobi
DialoGPT: You are a big guy


The repository is based on huggingface pytorch-transformer and OpenAI GPT-2, containing data extraction script, model training code and pretrained small (117M) medium (345M) and large (762M) model checkpoint.

The model is trained on 147M multi-turn dialogue from Reddit discussion thread.

# gpt colab 1

Make your own Rick Sanchez (bot) with Transformers and DialoGPT fine-tuning

https://colab.research.google.com/drive/15wa925dj7jvdvrz8_z3vU7btqAFQLVlG

# gpt colab 2

Rick and Morty : 2487

# more results

```

Hi
Hello
Today, I had a fight with my friend, and I'm not sure what to do now.
My friend broke my phone and I want to confront her but I'm not sure how
My cat died
I'm not sure how to be a good friend
How do I be a good friend?
How do I find friends?
Do I have to go to this dinner even though I don't want to?
You're pretty helpful
Bye


>> User:Hi
RickBot: !!!?!!,!!1!!>!!'!!If!!2!!6!!3!!5!!25!!
>> User:Hello
RickBot: !!!?!!You!!It!!Me!!
>> User:Today, I had a fight with my friend, and I'm not sure what to do now.
RickBot: I don’t know if I should talk to him or not
>> User:My friend broke my phone and I want to confront her but I'm not sure how
RickBot: What is your current situation? How do you feel about it?
>> User:My cat died
RickBot: !!!!'!!?!!What!!:!!Your!!Is!!,!!I!!If!!You!!Work!!The!!F!!This!!
>> User:I'm not sure how to be a good friend
RickBot: I really don’t know how to deal with this kind of situation
>> User:How do I be a good friend?
RickBot: You should be friends with him, and not just hang out
>> User:How do I find friends?
RickBot: You need to get out of the house and find some friends
>> User:Should I go to this dinner even though I don't want to?
RickBot: I think you guys are right
>> User:You're pretty helpful
RickBot: !!!?!!If!!,!!This!!Translation!!1!!Hey!!Work!!Language!!First!!>!!Break!!A!!
Bye


===

>> User:Hi
DialoGPT: Hi
>> User:Hello
DialoGPT: 
>> User:Today, I had a fight with my friend, and I'm not sure what to do now.
DialoGPT: What's the story with the guy?
>> User:My friend broke my phone and I want to confront her but I'm not sure how
DialoGPT: I'm sorry to hear that.
>> User:My cat died
DialoGPT: I'm sorry to hear that.
>> User:I'm not sure how to be a good friend
DialoGPT: I'm sorry to hear that.
>> User:How do I be a good friend?
DialoGPT: I'm sorry to be sorry
>> User:How do I find friends?
DialoGPT: I'm sorry to be sorry
>> User:Do I have to go to this dinner even though I don't want to?
DialoGPT: 
>> User:You're pretty helpful
DialoGPT: 
>> User:Bye
DialoGPT: 

===
with NO chat history

```
[Default DialoGPT]
>> User:Hi
DialoGPT: Hi
>> User:Hello
DialoGPT: 
>> User:Today, I had a fight with my friend, and I'm not sure what to do now.
DialoGPT: What's the story with the guy in the back?
>> User:My friend broke my phone and I want to confront her but I'm not sure how
DialoGPT: I'm not sure if you're joking or not, but I'm pretty sure that's not how it works.
>> User:My cat died
DialoGPT: I'm sorry for your loss.
>> User:I'm not sure how to be a good friend
DialoGPT: I'm not sure how to be a good friend
>> User:How do I be a good friend?
DialoGPT: I'm a good friend.
>> User:Should I go to this dinner even though I don't want to?
DialoGPT: I'm going to the dinner.
>> User:Do I have to go to this dinner even though I don't want to?
DialoGPT: I'm going to the dinner.
>> User:You're pretty helpful
DialoGPT: You're pretty stupid.
>> User:Bye
DialoGPT: I'm not going to be able to play for a few hours. I'll be back in about an hour.





[DialoGPT + Finetune on /r/relationships] [490 examples from 200 posts]
>> User:Hi
AdviceBot: !!!?!!If!!You!!Have!!Failed!!Me!!,!!I!!Work!!For!!The!!Hour!!Of!!Your!!Interview!!
>> User:Hello
AdviceBot: Hello friend
>> User:Today, I had a fight with my friend, and I'm not sure what to do now.
AdviceBot: What is the best way to resolve this?
>> User:My friend broke my phone and I want to confront her but I'm not sure how
AdviceBot: Do you have a relationship with her? If so what do you think is the best way to fix it?
>> User:My cat died
AdviceBot: !!!?!!You!!Hey!!Get out!!,!!'!!Work!!I!!Will!!This!!It!!Is!!The!!Fatal!!One!!Just!!In!!My!!Home!!For!!That!!M!!L!!And!!What!!“!!Did!!If!!Well!!He!!Expected!!So!!When!!To!!Meet!!A!!New!!Mom!!Trust!!
>> User:I'm not sure how to be a good friend
AdviceBot: I would ask her if she has a problem with you or if you need to talk
>> User:How do I be a good friend?
AdviceBot: It is not like you have to be a bad person to be friends with her
>> User:How do I find friends?
AdviceBot: You should be able to find some people to help you out
>> User:Do I have to go to this dinner even though I don't want to?
AdviceBot: It's like you don’t know what you’re doing
>> User:Should I go to this dinner even though I don't want to?
AdviceBot: I would not go to the dinner with anyone else
>> User:You're pretty helpful
AdviceBot: I just wanted to help
>> User:Bye
AdviceBot: I have a feeling I have to find out

[DialoGPT = off-the-shelf model, Advicebot adds finetuning on /r/relationships]

>> Hi
DialoGPT: Hi
AdviceBot: !!!?!!If!!You!!Have!!Failed!!Me!!,!!I!!Work!!For!!The!!Hour!!Of!!Your!!Interview!!

>> Hello
DialoGPT: 
AdviceBot: Hello friend

>> Today, I had a fight with my friend, and I'm not sure what to do now.
DialoGPT: What's the story with the guy in the back?
AdviceBot: What is the best way to resolve this?

>> My friend broke my phone and I want to confront her but I'm not sure how
DialoGPT: I'm not sure if you're joking or not, but I'm pretty sure that's not how it works.
AdviceBot: Do you have a relationship with her? If so what do you think is the best way to fix it?

>> My cat died
DialoGPT: I'm sorry for your loss.
AdviceBot: !!!?!!You!!Hey!!Get out!!,!!'!!Work!!I!!Will!!This!!It!!Is!!The!!Fatal!!One!!Just!!In!!My!!Home!!For!!That!!M!!L!!And!!What!!“!!Did!!If!!Well!!He!!Expected!!So!!When!!To!!Meet!!A!!New!!Mom!!Trust!!




==

    bot_input_ids = new_user_input_ids


>> User:Hi
DialoGPT: Hi
>> User:Hello
DialoGPT: I'm back!
>> User:Today, I had a fight with my friend, and I'm not sure what to do now.
DialoGPT: What's the story with the guy in the back?
>> User:My friend broke my phone and I want to confront her but I'm not sure how
DialoGPT: I'm not sure if you're joking or not, but I'm pretty sure that's not how it works.
>> User:My cat died
DialoGPT: I'm sorry for your loss.
>> User:It's my first time going to a party, what do I do there
DialoGPT: I'm not sure if you're joking or not, but you can't go to parties without a drink.
>> User:It's my first time going on a date, where should I go
DialoGPT: I'm not sure if you're joking or not, but I'm pretty sure you're joking.
>> User:I'm not sure how to be a good friend
DialoGPT: I'm not sure how to be a good friend
>> User:How do I find friends?
DialoGPT: I'm in the same boat.
>> User:You're pretty helpful
DialoGPT: You're pretty stupid.
>> User:Bye
DialoGPT: I'm not going to be able to play for a few hours. I'll be back in about an hour.


====


>> Hi 
AdviceBot: !!!?!!If!!,!!It!!M!!.!!'!!Work!! 

>> Hello 
AdviceBot: Hello hello 

>> Today, I had a fight with my friend, and I'm not sure what to do now. 
AdviceBot: You need to get over it 

>> My friend broke my phone and I want to confront her but I'm not sure how 
AdviceBot: Tell her to stop using her iphone 

>> My cat died 
AdviceBot: !!!?!!,!!'!!I!!Your!!F!! 

>> It's my first time going to a party, what do I do there 
AdviceBot: It sounds like you don't want to go to a political party 

>> It's my first time going on a date, where should I go 
AdviceBot: You can always come out 

>> I'm not sure how to be a good friend 
AdviceBot: I think you two need to be friends 

>> How do I find friends? 
AdviceBot: You have to ask yourself this very important question 

>> You're pretty helpful 
AdviceBot: I am not sure how to help you 

>> :Bye 
AdviceBot: !!!?!!If!!You!!Are!!A!!F!! Work!!,!!This!! Sounds!! Like!!I!!M!!S!! The!!L!!!!Is!!Me!! An!! In!!Wha !! It!!Removes !! First!!Things !! As !!N!!Did!! Change!!