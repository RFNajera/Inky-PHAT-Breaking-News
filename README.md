# Twitter Breaking News on the Inky PHAT from Pimoroni

Putting Twitter breaking news on display every few minutes on the Pimoroni Inky PHAT took some code modification, but what else is new, right?

## What you need
1. Raspberry Pi Zero W (or WH). If you get the W, then you'll have to do some soldering. No big deal.
2. [Pimoroni Inky PHAT](https://shop.pimoroni.com/products/inky-phat?variant=12549254217811)
3. 5V mini-USB power supply for the Raspberry
4. Micro SD card of at least 8GB capacity

## Initial Raspberry Pi Set Up
1. Install a lite version of the Raspbian Linux distribution on the SD card. I use Raspberry Pi's [own card imager](https://www.raspberrypi.org/software/). Choose a "lite" version because you don't want to bother with connecting a monitor, keyboard and mouse. We'll do all the work via SSH on a Mac.
2. When the image is installed, re-insert the SD card into your Mac if it was ejected. Open your Mac's terminal and navigate to your SD card:
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
3. Eject the SD card and insert it into the Raspberry Pi.
4. Connect the power to the Raspberry Pi and let it boot up. You'll know its fully booted up when the green LED stays solidly green.
5. Now, we need to find the IP address for your Raspberry Pi. For this, I used a program called Angry IP Scanner. You can use any IP scanner that will scan your network and find your Raspberry Pi's IP address. You'll know which one it is because the “host name” for the Raspberry Pi is "raspberry"-something. Once you have the IP address, go back to the terminal on your Mac.
6. Connect to your Raspberry Pi via SSH by typing into your terminal:
```
ssh YOUR.IP.ADDRESS.HERE -l pi
```
You will be asked for the password for the Raspberry Pi, which is the default “raspberry” (we'll change it in the next step).
7. Type the following command to open the configuration file in your Raspberry and change the password:
```python
sudo raspi-config
```
Once in the configuration, change the password.
8. Go back to the terminal and shutdown your Raspberry Pi:
```python
sudo shutdown -h
```
Take the power cord out and install the Inky PHAT.

## Attach Inky PHAT and Install Software
1. Attach the Inky PHAT on your Raspberry Pi, making sure it is sitting well in all the GPIO pins. ([Here is Pimoroni's instructions on how to do all this.](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat))
2. Plug in the power and make sure it boots up all the way before connecting via SSH to it again.
3. Install the Pimoroni software:
```python
curl https://get.pimoroni.com/inky | bash
```
This may take a few minutes. Be patient.
4.You can see in the instructions that you can play with some of the examples included in installation.
