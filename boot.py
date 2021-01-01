#!/usr/bin/env python

import time
from PIL import ImageFont, Image, ImageDraw
import os
import os.path
import ST7789 as ST7789
from socketIO_client import SocketIO
import sys

# get the path of the script
script_path = os.path.dirname(os.path.abspath(__file__))
# set script path as current directory
os.chdir(script_path)


# Create ST7789 LCD display class.
disp = ST7789.ST7789(
    rotation=90,  # Needed to display the right way up on Pirate Audio
    port=0,       # SPI port
    cs=1,         # SPI port Chip-select channel
    dc=9,         # BCM pin used for data/command
    backlight=13,
    spi_speed_hz=80 * 1000 * 1000
)

# Initialize display.
disp.begin()

WIDTH = 240
HEIGHT = 240
font_s = ImageFont.truetype(script_path + '/fonts/Roboto-Medium.ttf', 20)
font_m = ImageFont.truetype(script_path + '/fonts/Roboto-Medium.ttf', 24)
font_l = ImageFont.truetype(script_path + '/fonts/Roboto-Medium.ttf', 30)


def bootmessage():
    print('bootmessage called')
    disp.set_backlight(True)
    img = Image.new('RGBA', (240, 240), color=(0, 0, 0, 25))
    img = Image.open('images/default.jpg')
    draw = ImageDraw.Draw(img, 'RGBA')
    message = 'booting ...'
    draw.text((10, 200), message, font=font_m, fill=(255, 255, 255))
    disp.display(img)
    sys.exit()


try:
    bootmessage()
except SystemExit:
    print('Systemexit called')
    pass
