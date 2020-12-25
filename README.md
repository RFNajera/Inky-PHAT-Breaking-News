# Twitter Breaking News on the Inky PHAT from Pimoroni

![Image of The PHAT at Work](https://github.com/RFNajera/Inky-PHAT-Breaking-News/blob/main/breaking_news_inky.jpg)

Putting Twitter breaking news on display every few minutes on the Pimoroni Inky PHAT took some code modification, but what else is new, right?

## What you need
* Raspberry Pi Zero W (or WH). If you get the W, then you'll have to do some soldering. No big deal.
* [Pimoroni Inky PHAT](https://shop.pimoroni.com/products/inky-phat?variant=12549254217811)
* 5V mini-USB power supply for the Raspberry
* Micro SD card of at least 8GB capacity

## Initial Raspberry Pi Set Up
* Install a lite version of the Raspbian Linux distribution on the SD card. I use Raspberry Pi's [own card imager](https://www.raspberrypi.org/software/). Choose a "lite" version because you don't want to bother with connecting a monitor, keyboard and mouse. We'll do all the work via SSH on a Mac.
* When the image is installed, re-insert the SD card into your Mac if it was ejected. Open your Mac's terminal and navigate to your SD card:
```
cd /Volumes/boot
```
Once in the boot folder, you will now create an SSH file for you to be able to connect to your Raspberry via SSH once you boot it up:
```
touch ssh
```
You will also want to create a WPA supplicant file to tell the Raspberry how to connect to your home wifi:
```
sudo nano wpa_supplicant.conf
```
When nano opens, write the following code and make sure to replace your wifi network name and password:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
 ssid="Name of your wireless LAN" # Remember to replace the name of your wireless network here
 psk="Password for your wireless LAN" # Remember to replace with the password for your wireless here
}
```
It goes without saying that the name of your network and the password are in the file, and they're not encrypted. So be extra careful if you're using an open network or if you lose the card.
* Eject the SD card and insert it into the Raspberry Pi.
* Connect the power to the Raspberry Pi and let it boot up. You'll know its fully booted up when the green LED stays solidly green.
* Now, we need to find the IP address for your Raspberry Pi. For this, I used a program called Angry IP Scanner. You can use any IP scanner that will scan your network and find your Raspberry Pi's IP address. You'll know which one it is because the “host name” for the Raspberry Pi is "raspberry"-something. Once you have the IP address, go back to the terminal on your Mac.
* Connect to your Raspberry Pi via SSH by typing into your terminal:
```
ssh YOUR.IP.ADDRESS.HERE -l pi
```
You will be asked for the password for the Raspberry Pi, which is the default “raspberry” (we'll change it in the next step).
* Type the following command to open the configuration file in your Raspberry and change the password:
```python
sudo raspi-config
```
Once in the configuration, change the password.
* Go back to the terminal and shutdown your Raspberry Pi:
```python
sudo shutdown -h
```
Take the power cord out and install the Inky PHAT.

## Attach Inky PHAT and Install Software
* Attach the Inky PHAT on your Raspberry Pi, making sure it is sitting well in all the GPIO pins. ([Here is Pimoroni's instructions on how to do all this.](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat))
* Plug in the power and make sure it boots up all the way before connecting via SSH to it again.
* Install the Pimoroni software:
```python
curl https://get.pimoroni.com/inky | bash
```
This may take a few minutes. Be patient.
* You can see in the instructions that you can play with some of the examples included in installation. This will help you test the software and make sure you have everything set up and plugged in right. If you need to install some more packages, make sure you do, of course.

## Get Twitter API Keys
* Go to [Twitter's Developer Site](https://developer.twitter.com/) and sign up for a developer account. Make sure you answer all the questions to the best of your ability. It may take a few hours for them to give you an account. Once you have the account, register your app.
* I told Twitter that this is just a hobby, because it is. Don't lie! If they catch you using this for some commercial enterprise, and you said you were doing hobby work, you'll lose your ability to use the API.

## Create a Python Script Like the “config.py” File in This Repository, or Clone It
* Type the following in the terminal to create the file:
```python
sudo nano config.py
```
Copy the contents of the .py file in this repository, replacing the consumer key and secret and the access key and secret that you got when you signed up for access to the Tiwtter API.
* Hit control+X to exit, and make sure you save it.

## Create a Python Script Like the “breaking.py” File for Your Breaking News
* Type the command above to create another script. I named mine “breaking.py”.
```python
sudo nano breaking.py
```
* Change anything in there you want to change. I use the [Associated Press' Twitter Stream](https://twitter.com/ap) to get the latest tweet, and I filter out retweets and replies. You may want to use BBC News, NBC, ABC, CNN, Fox, etc. It's up to you.
* Hit control+X to exist.

## You'll Need Tweepy
* As you can see in the scripts, you need to install Tweepy, so back at the terminal, type:
```python
sudo pip install tweepy
```
* You can read all about Tweepy on [its documentation site](http://docs.tweepy.org/en/latest/install.html).

## Try Out Your Script
* Go ahead and try out your breaking news script:
```python
python3 breaking.py
```
If everything is working, the Inky PHAT will refresh and show the latest tweet from the source you chose. Note that the terminal will also show that message.

## Didn't Work?
* If it didn't work, you might want to make sure that you have all the necessary modules installed. Note that I'm using PIL (Python Image Library), font_hanken_grotesk, and Tweepy.
* Note that I am not a professional Python coder, and that I adapted a lot of the code for these from other sources. I tried to annotate the code as much as possible to show you how it is working.
* There is plenty of help online if you need it.
