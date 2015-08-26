from PIL import Image, ImageDraw
import random
from math import *

image = Image.open('me.jpg')
(width, height) = image.size
def greenscreen(image, startx, starty, endx, endy, leniency, (r, g, b), (inr,ing,inb)):
    
    width, height = image.size
    if (r+leniency, g+leniency, b+leniency) > (255,255,255):
        pluslein = (255, 255, 255)
    else:
        pluslein = (r+leniency, g+leniency, b+leniency)
    minuslien = (r-leniency, g-leniency, b-leniency)
    for x in xrange(startx, endx):
        for y in xrange(starty, endy):
            if image.getpixel((x,y)) < pluslein and image.getpixel((x,y)) > minuslien:
                image.putpixel((x,y), (inr,ing,inb))


def greenerscreen(image, startx, starty, endx, endy, (inr,ing,inb)):
    for x in xrange(startx, endx):
        for y in xrange(starty, endy):
            diff = abs(image.getpixel((x,y))[1] - image.getpixel((x,y))[0])
            if  diff < 30 and (image.getpixel((x,y))[0] - image.getpixel((x,y))[2] > 80):
                image.putpixel((x,y), (inr,ing,inb))
def breakit(image, startx,endx,starty,endy):
     """ shifts left of the picture to the right randomly"""
    
     (width, height) = image.size
     for x in xrange(startx,endx):
        for y in xrange(starty,endy):
               fromX = x
               fromY = starty
               (newRed, newGreen, newBlue)=image.getpixel((fromX, fromY))
               image.putpixel((x,y),(newRed, newGreen, newBlue));

def shifter(image):
     """ Copies the left half of the picture to the right half"""
     (width, height) = image.size
     rand = random.randint(0,10)
     for x in range(width/2, width):
          for y in range(height):
               fromX = x - (width/2)
               fromY = y
               (newRed, newGreen, newBlue)=image.getpixel((fromX, fromY))
               image.putpixel((x,y),(newRed, newGreen, newBlue));
     return image


def algeart(image, startx,endx,starty,endy):
    for x in xrange(startx,endx):
        for y in xrange(starty,endy):
            (origr, origg, origb) = image.getpixel((x,y))
            r = int(tan(origr)*150 + 100)
            g = int(tan(origg)*100 + 100)
            b = int(sin(origb/4)*200 + 100)
            image.putpixel((x,y), (r,g,b))

def hyperinflate(image, startx,endx,starty,endy):
    (width, height) = image.size
    for x in xrange(width):
        for y in xrange(height):
            (origr, origg, origb) = image.getpixel((x,y))
            r = int(origr * 1.5)
            g = int(origg * 1.5)
            b = int(origb * 1.5)
            image.putpixel((x,y), (r,g,b))
