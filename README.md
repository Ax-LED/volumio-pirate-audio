## Update 07. January 2021
You don't have to use this repository anymore, as "pirateaudio" is now available as plugin via volumio GUI
(see plugin section (miscellanea/pirateaudio) in volumio)

<b>Notes:</b>
- You have to restart volumio after installation, as the install process adds informations to /boot/userconfig.txt, which are only used after a restart.
- Output devices should be set to "HiFiBerry DAC" (if not already set)
- Volume setting -> type of mixer should be set to "Software" (if not already set)

# volumio-pirate-audio
Python code (plugin) to use pirate audio dac with volumio (including display and the 4 buttons) and a raspberry pi.
## Pictures
Player Mode:<br>
![Volumio pirate audio picture 1](https://raw.githubusercontent.com/Ax-LED/volumio-pirate-audio/master/pictures/picture_player_mode.jpg)<br>
Menu Mode:<br>
![Volumio pirate audio picture 2](https://raw.githubusercontent.com/Ax-LED/volumio-pirate-audio/master/pictures/picture_menu_mode.jpg)<br>
Browselibrary Mode:<br>
![Volumio pirate audio picture 3](https://raw.githubusercontent.com/Ax-LED/volumio-pirate-audio/master/pictures/picture_browselibrary_mode.jpg)
## Installation
### Clone this repository
Clone this repository to `/home/volumio/` on your raspberry pi.
````
git clone https://github.com/Ax-LED/volumio-pirate-audio
````
### Set permitions/rights so files will be executable:
`sudo chmod +x /home/volumio/volumio-pirate-audio/boot.py`<br>
`sudo chmod +x /home/volumio/ volumio-pirate-audio/display.py`
### Modifiy /boot/config.txt by adding following lines:
`sudo nano /boot/config.txt`
````
### AxLED ####
dtoverlay=hifiberry-dac
gpio=25=op,dh
dtparam=spi=on
### AxLED - Fix for Button X Y of pirate audio ####
gpio=16=pu
gpio=20=pu
````
<b>Reason:</b>
- GPIO 25 settings are important for the amp
- to set PullUp of GPIO PINS 16 and 20 so they work
### Install depencies:
````
sudo apt-get update
sudo apt-get install -y python-rpi.gpio python-spidev python-pip python-pil python-numpy
sudo pip install st7789
sudo pip install socketIO-client
````
### Consider python files for autostart
Modify /etc/rc.local by adding following lines: `sudo nano /etc/rc.local`
````
/home/volumio/volumio-pirate-audio/boot.py &
/home/volumio/volumio-pirate-audio/display.py &
exit 0
````
<b>Note:</b> The & (ampersand) at the end is important. Add the lines mentioned above <u>before</u> „exit 0“
### Final:
Reboot your pi `sudo reboot`

