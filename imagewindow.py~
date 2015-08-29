import Tkinter 
from PIL import Image, ImageTk
import random
import tkSimpleDialog
from math import *




imagelist = []
operationlist = []
numdegrades = 7
filename = ''
filetype = ''
picname = raw_input("What is the name of your picture, friend? ")
im = Image.open(picname)
root = Tkinter.Tk()
root.title("GLOTCH")
tkimage = ImageTk.PhotoImage(im)
canvas = Tkinter.Label(root, image=tkimage)
canvas.grid(row=0, column=2, columnspan=10, rowspan=10)
pBits = im.convert('RGB')

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

def blurer(im):
    imsize = im.size
    (width, height) = imsize
    im2 = Image.new('RGB', (width,height))
    for x in xrange(0,width - 2):
        for y in xrange(0,height - 2):
            (baseR, baseG, baseB) = im.getpixel((x,y))
            (rightR, rightG, rightB) = im.getpixel((x + 2,y))
            (lowR, lowG, lowB) = im.getpixel((x,y + 2))
            avgR = (baseR + rightR + lowR) / 3
            avgG = (baseG + rightG + lowG) / 3
            avgB = (baseB + rightB + lowB) / 3
            im2.putpixel((x + 1,y + 1), (avgR, avgG, avgB))
    for x in [0, width - 1]:
        for y in xrange (0, height):
            (baseR, baseG, baseB) = im.getpixel((x,y))
            im2.putpixel((x,y ), (baseR, baseG, baseB))
    for y in [0, height - 1]:
        for x in xrange (0, width):
            (baseR, baseG, baseB) = im.getpixel((x,y))
            im2.putpixel((x,y), (baseR, baseG, baseB))
    
    return im2

def graindrip(im, dripamount, height_variance):
    imsize = im.size
    (width, height) = imsize
    if height_variance > height:
        height_variance = height
    for x in xrange(0, width):
        if random.random() < dripamount:
            for y in xrange(0, height - random.randint(0,height_variance)):
                if random.random() < dripamount:
                    (origr, origg, origb) = im.getpixel((x ,y))
                    r = abs(origr-255)
                    g = abs(origg-255)
                    b = abs(origb- 255)
                    im.putpixel((x,y), (r,g,b))
    return im

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

def blur():
    global im
    im2 = blurer(im)
    im = im2
    tkimage2 = ImageTk.PhotoImage(im2)
    canvas.configure(image = tkimage2)
    canvas.image = tkimage2
    imagecopy = im2.copy()
    imagelist.append(imagecopy)
    operationlist.append('blurer')


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

class DripDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Negative Drip")

        top.resizable(0,0)

        Tkinter.Label(top, text="Gain Amount (0.0 to 1.0):").pack()

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack()

        Tkinter.Label(top, text="Height Variance (Pixel amt):").pack()

        self.entry2 = Tkinter.Entry(top)
        self.entry2.pack()


        button = Tkinter.Button(top, text="Okay", command=self.graindrip)
        button.pack()

    def graindrip(self):
        Gain = float(self.entry1.get())
        Height = int(self.entry2.get())
        im2 = graindrip(im, Gain, Height)
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('ndrip')
        self.top.destroy()

class SaveDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Save")

        top.resizable(0,0)

        Tkinter.Label(top, text="Filename:").pack()

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack()

        Tkinter.Label(top, text="Filetype:").pack()

        self.entry2 = Tkinter.Entry(top)
        self.entry2.pack()

        button = Tkinter.Button(top, text="Save", command=self.save)
        button.pack()

    def save(self):
        filename = self.entry1.get()
        filetype = self.entry2.get()
        im.save(str(filename),format = str(filetype))
        self.top.destroy()

def savediag():
    savdiag = SaveDialog(root)

def dripdiag():
    dripdiag = DripDialog(root)


Tkinter.Button(text="Undo", fg="black", command = undo).grid(row = 0, column = 0)
Tkinter.Button(text="Shift", fg="black",command = shifter).grid(row = 1, column = 0)
Tkinter.Button(text="Degrade", fg="black", command = degrader).grid(row = 2, column = 0)
Tkinter.Button(text="Tear", fg="black", command = tear).grid(row = 3, column = 0)
Tkinter.Button(text="Blur", fg="black", command = blur).grid(row = 4, column = 0)
Tkinter.Button(text="Save", fg="black", command = savediag).grid(row = 5, column = 0)
Tkinter.Button(text=" N. Drip", fg="black", command = dripdiag).grid(row = 6, column = 0)

root.mainloop()


