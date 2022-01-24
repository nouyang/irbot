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


### example errors
- NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
- Could not use `sudo ubuntu-drivers autoinstall` (got E: Unable to correct problems, you have held broken packages.)

