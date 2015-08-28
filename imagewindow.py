import Tkinter 
from PIL import Image, ImageTk
import random


imagelist = []
operationlist = []
numdegrades = 7
picname = raw_input("what is your command master? ")
im = Image.open(picname)
root = Tkinter.Tk()  
tkimage = ImageTk.PhotoImage(im)
canvas = Tkinter.Label(root, image=tkimage)
canvas.pack()

def shiftover(image):
    """ Copies the left half of the picture to the right half"""
    (width, height) = image.size
    start = 0
    end = random.randint(0,height)
    while end < height:
        if random.random() > .5:
            randheight = random.randint(0,height/6)
            randwidth = random.randint(0,width/2)
            for x in xrange(randwidth, width):
                for y in xrange(start, end):
                    (r,g,b) = image.getpixel((x,y))
                    image.putpixel((x-randwidth,y), (r,g,b))
            start += end
            end += randheight
        else:
            randheight = random.randint(0,height)
            randwidth = random.randint(0,width/2)
            for x in xrange(0, randwidth):
                for y in xrange(start, end):
                    (r,g,b) = image.getpixel((x,y))
                    image.putpixel((x + randwidth,y), (r,g,b))
            start += end
            end += randheight
        if end >= height:
            end = height
            if random.random() > .5:
                randheight = random.randint(0,height/6)
                randwidth = random.randint(0,width/2)
                for x in xrange(randwidth, width):
                    for y in xrange(start, end):
                        (r,g,b) = image.getpixel((x,y))
                        image.putpixel((x-randwidth,y), (r,g,b))
                start += end
                end += randheight
            else:
                randheight = random.randint(0,height)
                randwidth = random.randint(0,width/2)
                for x in xrange(0, randwidth):
                    for y in xrange(start, end):
                        (r,g,b) = image.getpixel((x,y))
                        image.putpixel((x + randwidth,y), (r,g,b))
                start += end
                end += randheight
    return image

    

def shiftNBitsTo8( num, N ):
    return num << 8 - N

def mostSignificantN( num, N):
    num = num >> (8 - N)
    return num

def getLeastSignificantN( num, N ):
    return num % (2 ** N)

def degradeColors( pic, N):
  picCopy = Image.new('RGB', pic.size, (0, 0, 0))
  for x in range(pic.size[0]):
    for y in range(pic.size[1]):
      (r,g,b) = pic.getpixel( (x, y) )
      r =  shiftNBitsTo8(getLeastSignificantN(r,N), N)
      g =  shiftNBitsTo8(getLeastSignificantN(g,N), N)
      b =  shiftNBitsTo8(getLeastSignificantN(b,N), N)
      picCopy.putpixel( (x,y), ( r, g, b ) )
  return picCopy


def tearover(image):
    """ Copies the left half of the picture to the right half"""
    (width, height) = image.size
    start = 0
    end = random.randint(0,height)
    while end < height:
        if random.random() > .5:
            randheight = random.randint(0,height/6)
            randwidth = random.randint(0,width/2)
            for x in xrange(randwidth, width,2):
                for y in xrange(start, end,2):
                    (r,g,b) = image.getpixel((x,y))
                    r = int(r * 4)
                    image.putpixel((x-randwidth,y), (r,g,b))
            start += end
            end += randheight
        else:
            randheight = random.randint(0,height)
            randwidth = random.randint(0,width/2)
            for x in xrange(0, randwidth,2):
                for y in xrange(start, end,2):
                    (r,g,b) = image.getpixel((x,y))
                    b = int(b * 4)
                    image.putpixel((x + randwidth,y), (r,g,b))
            start += end
            end += randheight
        if end >= height:
            end = height
            if random.random() > .5:
                randheight = random.randint(0,height/6)
                randwidth = random.randint(0,width/2)
                for x in xrange(randwidth, width,2):
                    for y in xrange(start, end,2):
                        (r,g,b) = image.getpixel((x,y))
                        r = int(r * 4)
                        image.putpixel((x-randwidth,y), (r,g,b))
                start += end
                end += randheight
            else:
                randheight = random.randint(0,height)
                randwidth = random.randint(0,width/2)
                for x in xrange(0, randwidth,2):
                    for y in xrange(start, end,2):
                        (r,g,b) = image.getpixel((x,y))
                        b = int(b * 4)
                        image.putpixel((x + randwidth,y), (r,g,b))
                start += end
                end += randheight
            break
    return image

def shifter():
    im2 = shiftover(im)
    tkimage2 = ImageTk.PhotoImage(im2)
    canvas.configure(image = tkimage2)
    canvas.image = tkimage2
    imagecopy = im2.copy()
    imagelist.append(imagecopy)
    operationlist.append('shifter')

def degrader():
    global numdegrades
    global im
    if numdegrades > 4:
        im2 = degradeColors(im, numdegrades)
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        numdegrades = numdegrades - 1
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('degrader')

def tear():
    im2 = tearover(im)
    tkimage2 = ImageTk.PhotoImage(im2)
    canvas.configure(image = tkimage2)
    canvas.image = tkimage2
    imagecopy = im2.copy()
    imagelist.append(imagecopy)
    operationlist.append('tear')

def undo():
    global im
    global numdegrades
    if len(imagelist) > 0:
        lastoper = operationlist.pop()
        if lastoper == 'degrader':
            numdegrades += 1
        im = imagelist[-1]
        im2 = imagelist.pop()
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
    else:
        im = Image.open(picname)
        tkimage = ImageTk.PhotoImage(im)
        canvas.configure(image = tkimage)
        canvas.image = tkimage
        
Tkinter.Button(text="Shift", fg="black",command = shifter).pack(side = 'left')
Tkinter.Button(text="Undo", fg="black", command = undo).pack(side = 'right')
Tkinter.Button(text="Degrade", fg="black", command = degrader).pack(side = 'right')
Tkinter.Button(text="Tear", fg="black", command = tear).pack(side = 'left')
root.mainloop()


