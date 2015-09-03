
import Tkinter
from PIL import Image
import random

def seamer(im, inter):
    '''takes parameters im and interpolation'''
    def putseamvert(im, x ,y):
        imsize = im.size
        (width, height) = imsize
        if height > 900:
	    height = 900
        if y == height - 1:
            im.putpixel((x,y), (255,0,0))
            return
        elif x + 1 >= width - 1:
            (value2) = im.getpixel((x,y + 1))[0]
            (value4) = im.getpixel((x - 1,y+1))[0]
            minvalue = max(value2, value4)
            value3 = 0
        elif x - 1 <= 1:
            (value2) = im.getpixel((x,y + 1))[0]
            (value3) = im.getpixel((x + 1,y+1))[0]
            minvalue = max(value2, value3)
            value4 = 0
        else:
            (value2) = im.getpixel((x,y + 1))[0]
            (value3) = im.getpixel((x + 1,y+1))[0]
            (value4) = im.getpixel((x - 1,y+1))[0]
            minvalue = max(value2, value3, value4)
        if minvalue == value2:
            putseamvert(im, x, y + 1)
        elif minvalue == value3:
            putseamvert(im, x + 1, y + 1)
        elif minvalue == value4:
            putseamvert(im, x - 1, y + 1)

        im.putpixel((x,y), (255,0,0))
        return im

    def putseamhori(im, x ,y):
        (width, height) = im.size
        if width > 900:
	    width = 900
        if x == width - 1:
            im.putpixel((x,y), (255,0,0))
            return
        elif y + 1 >= height - 1:
            (value2) = im.getpixel((x + 1,y))[0]
            (value3) = im.getpixel((x + 1,y - 1))[0]
            minvalue = max(value2, value3)
            value4 = 0
        elif y - 1 <= 1:
            (value2) = im.getpixel((x + 1,y))[0]
            (value4) = im.getpixel((x + 1,y + 1))[0]
            minvalue = max(value2, value4)
            value3 = 0
        else:
            (value2) = im.getpixel((x + 1,y))[0]
            (value3) = im.getpixel((x + 1,y - 1))[0]
            (value4) = im.getpixel((x + 1,y + 1))[0]
            minvalue = max(value2, value3, value4)
        if minvalue == value2:
            putseamhori(im, x + 1, y)
        elif minvalue == value3:
            putseamhori(im, x + 1, y - 1)
        elif minvalue == value4:
            putseamhori(im, x + 1, y + 1)

        im.putpixel((x,y), (255,0,0))
        return im


    def cutter(im, inter):
                    
        im2 = im.copy()
        (width, height) = im.size

        if random.random() > .5:
            im2 = putseamvert(im2, (random.randint(0,width)), 0)
            for y in xrange(0,height):
                for x in xrange(0,width):
                        if im2.getpixel((x,y)) == (255,0,0):
                            for i in xrange(y + (height/inter), height):
                                (r,g,b) = im.getpixel((x, i))
                                im.putpixel((x,i - (height/inter)),(r,g,b))
        else:
            im2 = putseamhori(im2, 0, (random.randint(0,height)))
            for x in xrange(0,width):
                for y in xrange(0,height):
                        if im2.getpixel((x,y)) == (255,0,0):
                            for i in xrange(x + (width/inter), width):
                                (r,g,b) = im.getpixel((i,y))
                                im.putpixel((i - (width/inter),y),(r,g,b))

        return im

    return cutter(im, inter)

