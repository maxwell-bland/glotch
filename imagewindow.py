import Tkinter, tkFileDialog, threading
from PIL import Image, ImageTk
import random
import tkSimpleDialog
from math import *
import ttk
import time
from seamer import seamer

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
            randheight = random.randint(0,height/6)
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

def pixelate(im, amt):
    imsize = im.size
    (width, height) = imsize
    if amt == 0:
        amt = 1
    if width % amt:
        width = width - width % amt
    if height % amt:
        height = height - height % amt
    im2 = Image.new('RGB', (width,height))
    for x in xrange(0,width,amt):
        for y in xrange(0,height,amt):
            (baseR, baseG, baseB) = im.getpixel((x,y))
            for i in xrange(0, amt):
                for j in xrange(0, amt):
                    im2.putpixel((x + i,y + j), (baseR, baseG, baseB))

    return im2

def disburse(im, iters, sizex, sizey):
    imsize = im.size
    (width, height) = imsize
    if sizex > width:
        sizex = random.randint(0,width)
    if sizey > height:
        sizey = random.randint(0,height)
    im2 = im.copy()
    for iter in xrange(iters):
        startx1 = random.randint(0, width - sizex)
        starty1 = random.randint(0, height - sizey)
        startx2 = random.randint(0, width - sizex)
        starty2 = random.randint(0, height - sizey)
        for i in xrange(0, random.randint(0,sizex)):
            for j in xrange(0, sizey):
                (R1, G1, B1) = im.getpixel((startx1 + i,starty1 + j))
                (R2, G2, B2) = im.getpixel((startx2 + i,starty2 + j))
                im2.putpixel((startx2 + i,starty2 + j), (R1, G1, B1))
                im2.putpixel((startx1 + i,starty1 + j), (R2, G2, B2))

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
    if numdegrades > 5:
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


class DisburseDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Disburse")

        top.resizable(0,0)

        Tkinter.Label(top, text="Iterations:").pack(padx =10, pady= (5,1))

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack(padx =10, pady= (0,5))

        Tkinter.Label(top, text="Width Variance:").pack(padx =10, pady= (5,1))

        self.entry2 = Tkinter.Entry(top)
        self.entry2.pack(padx =10, pady= (0,5))

        Tkinter.Label(top, text="Height Variance:").pack(padx =10, pady= (5,1))

        self.entry3 = Tkinter.Entry(top)
        self.entry3.pack(padx =10, pady= (0,5))

        button = Tkinter.Button(top, text="OK", command=self.disbursed)
        button.pack(padx =10, pady= 5)

        top.iconbitmap("@icon.xbm")

        
    def disbursed(self):
        global im
        Iter = int(self.entry1.get())
        Width = int(self.entry2.get())
        Height = int(self.entry3.get())
        im2 = disburse(im, Iter, Width, Height)
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('disburse')
        self.top.destroy()


class DripDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Negative Drip")

        top.resizable(0,0)

        Tkinter.Label(top, text="Gain Amount (0.0 to 1.0):").pack(padx =10, pady= 5)

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack(padx =10, pady= (0,5))

        Tkinter.Label(top, text="Height Variance (Pixel amt):").pack()

        self.entry2 = Tkinter.Entry(top)
        self.entry2.pack(padx =10, pady= 5)

        button = Tkinter.Button(top, text="OK", command=self.graindrip)
        button.pack(padx =10, pady= 5)

        top.iconbitmap("@icon.xbm")

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


class SeamDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Seam Cut")

        top.resizable(0,0)

        Tkinter.Label(top, text="Interpolation:").pack(padx =10, pady= 5)

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack(padx =10, pady= (0,5))

        button = Tkinter.Button(top, text="OK", command=self.seam)
        button.pack(padx =10, pady= (0,5))

        top.iconbitmap("@icon.xbm")

    def seam(self):
        global im
        amt = (abs(int(self.entry1.get())) + 1)
        im2 = seamer(im, amt)
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('seamer')
        self.top.destroy()

class PixelDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Pixelate")

        top.resizable(0,0)

        Tkinter.Label(top, text="Pixelate amt:").pack(padx =10, pady= 5)

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack(padx =10, pady= (0,5))

        button = Tkinter.Button(top, text="OK", command=self.Pixelize)
        button.pack(padx =10, pady= (0,5))

        top.iconbitmap("@icon.xbm")

    def Pixelize(self):
        global im
        amt = int(self.entry1.get())
        im2 = pixelate(im, amt)
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('pixelate')
        self.top.destroy()

class RandDialog:

    def __init__(self, parent):
        
        top = self.top = Tkinter.Toplevel(parent)

        top.title("Randomize")

        top.resizable(0,0)

        label = self.label = Tkinter.Label(top, text="Iterations:")
        label.pack(padx = 10, pady = 5)
        

        entry1 = self.entry1 = Tkinter.Entry(top)
        entry1.pack(padx = 10, pady = 5)

        button = self.button = Tkinter.Button(top, text="OK", command=self.random)
        button.pack(pady = 5)

        top.iconbitmap("@icon.xbm")

    def step(self):
        self.progressbar.step(10)
        root.update_idletasks()
        time.sleep(3)
        
    def random(self):

        iter = int(self.entry1.get())
        self.button.destroy()
        self.label.pack_forget()
        self.entry1.pack_forget()
        
        self.loading = Tkinter.Label(self.top, text="Loading...").pack(padx = 10, pady = 5)
        progressbar = self.progressbar = ttk.Progressbar(master = self.top, orient='horizontal', length=200, mode='determinate')
        progressbar.pack(padx = 10, pady = 5)
        cancelbutton = self.cancelbutton = Tkinter.Button(self.top, text="Cancel", command=self.cancel)
        cancelbutton.pack(pady = 5)
        root.update_idletasks()
        for x in xrange(iter):
            randomize()
            self.progressbar.step(100/iter)
            root.update()
            if self.top == None:
                return
        self.top.destroy()

    def cancel(self):
        if not self.top == None:
            self.top.destroy()
            self.top = None

def randomize():
    global im
    listoper = [shifter,degrader,tear,blur, pixelate, undo, disburse, graindrip, seamer]
    randint1 = random.randint(0, 30)
    randint2 = random.randint(0,2000)
    randint3 = random.randint(0,2000)
    cmd = random.choice(listoper)
    if cmd == pixelate:
        im2 = pixelate(im, randint1)
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('pixelate')
    elif cmd == disburse:
        im2 = disburse(im, randint1, randint2, randint3)
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('disburse')
    elif cmd == graindrip:
        Gain = float(random.random())
        Height = int(randint2)
        im2 = graindrip(im, Gain, Height)
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('ndrip')
    elif cmd == seamer:
        im2 = seamer(im, random.randint(1, 300))
        im = im2
        tkimage2 = ImageTk.PhotoImage(im2)
        canvas.configure(image = tkimage2)
        canvas.image = tkimage2
        imagecopy = im2.copy()
        imagelist.append(imagecopy)
        operationlist.append('seamer')
    else:
        cmd()


        
class SaveDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Save")

        top.resizable(0,0)

        Tkinter.Label(top, text="Filename:").pack(padx =10, pady= 5)

        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack(padx =10, pady= (0,5))

        Tkinter.Label(top, text="Filetype:").pack()

        self.entry2 = Tkinter.Entry(top)
        self.entry2.pack(padx =10, pady= 5)

        button = Tkinter.Button(top, text="Save", command=self.save)
        button.pack(padx =10, pady= 5)

        top.iconbitmap("@icon.xbm")

    def save(self):
        filename = self.entry1.get()
        filetype = self.entry2.get()
        im.save(str(filename),format = str(filetype))
        self.top.destroy()

class SeedChangeDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Change Seed")

        top.resizable(0,0)

        Tkinter.Label(top, text="Seed:").pack( pady=(5, 0))
        self.entry1 = Tkinter.Entry(top)
        self.entry1.pack(padx = 20, pady = 5)

        def inputrand():
            self.entry1.delete(0,9999999)
            self.entry1.insert(0, random.randint(0,9999999))
            
        Tkinter.Button(top, text="Random Seed",command = inputrand).pack(pady = 5)

        button = Tkinter.Button(top, text="OK", command = self.changeseed)
        button.pack(pady = 5)

        top.iconbitmap("@icon.xbm")

    def changeseed(self):
        global seed, seedlabel
        try:
            seed = int(self.entry1.get())
            random.seed(seed)
            seedlabel.config(text = "Seed #: " + str(seed))
            print "Your new seed is: " + str(seed)
            root.update()
            self.top.destroy()
        except ValueError:
            InvalidSeed(root)
        
        

class FileDialog:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("File")

        top.resizable(0,0)

        button = Tkinter.Button(top, text="Open New", command=self.opennew)
        button.pack(padx =30, pady= (10,0))

        button = Tkinter.Button(top, text="Save", command=self.savediag)
        button.pack(padx =30, pady= 10)

        button = Tkinter.Button(top, text="Change Seed", command=self.changeseed)
        button.pack(padx =30, pady= (0,10))

        top.iconbitmap("@icon.xbm")

    def opennew(self):
        self.top.destroy()
        opennew()
        
    def savediag(self):
        self.top.destroy()
        savediag()

    def changeseed(self):
        seedchange = SeedChangeDialog(self.top)
        
        

class InvalidSeed:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Error 1337")

        top.resizable(0,0)

        top.iconbitmap("@icon.xbm")

        Tkinter.Label(top, text="ACK!", font = ('Helvetica', 15, "bold")).pack(padx = 20, pady = (10,0))
        Tkinter.Label(top, text="Put some good seed in me.", font = (10)).pack(padx = 20, pady = (0,10))


class InvalidImage:

    def __init__(self, parent):

        top = self.top = Tkinter.Toplevel(parent)

        top.title("Error 69")

        top.resizable(0,0)

        top.iconbitmap("@icon.xbm")

        Tkinter.Label(top, text="ACK!", font = ('Helvetica', 15, "bold")).pack(padx = 20, pady = (10,0))
        Tkinter.Label(top, text="I can't jerk off to this!", font = (10)).pack(padx = 20, pady = (0,10))

class InvalidImageSize:

    def __init__(self):

        top = self.top = Tkinter.Tk()

        top.title("Error 1234")

        top.resizable(0,0)

        top.iconbitmap("@icon.xbm")

        Tkinter.Label(top, text="ACK!", font = ('Helvetica', 15, "bold")).pack(padx = 20, pady = (10,0))
        Tkinter.Label(top, text="It is too big for me to hold!", font = (10)).pack(padx = 20, pady = (0,10))


def seamdiag():
    seamdiag = SeamDialog(root)

def randdiag():
    randdiag = RandDialog(root)

def filediag():
    filediag = FileDialog(root)

def savediag():
    savdiag = SaveDialog(root)

def dripdiag():
    dripdiag = DripDialog(root)

def pixeldiag():
    pixeldiag = PixelDialog(root)

def disbursediag():
    disdiag = DisburseDialog(root)
            
def startit():
    global imagelist, operationlist, seed, picname, numdegrades, im, root, tkimage, canvas, seedlabel
    imagelist = []
    operationlist = []
    random.seed(seed)
    numdegrades = 7
    root = Tkinter.Tk()
    root.title("GLOTCH")
    tkimage = ImageTk.PhotoImage(im)
    if im.size[0] * im.size[1] < 950 * 950:
        canvas = Tkinter.Label(root, image=tkimage, width = im.size[0], height = im.size[1])
        canvas.grid(row=0, column=2, columnspan=10, rowspan=12)
        b = Tkinter.Button(text = "File", fg = "black", command = filediag).grid(row = 0, column = 0)
        b1 = Tkinter.Button(text="Undo", fg="black", command = undo).grid(row = 1, column = 0)
        b2 = Tkinter.Button(text="Shift", fg="black",command = shifter).grid(row = 2, column = 0)
        b3 = Tkinter.Button(text="Degrade", fg="black", command = degrader).grid(row = 3, column = 0)
        b4 = Tkinter.Button(text="Tear", fg="black", command = tear).grid(row = 4, column = 0)
        b5 = Tkinter.Button(text="Blur", fg="black", command = blur).grid(row = 5, column = 0)
        b7 = Tkinter.Button(text="N. Drip", fg="black", command = dripdiag).grid(row = 6, column = 0)
        b8 = Tkinter.Button(text="Pixelate", fg="black", command = pixeldiag).grid(row = 7, column = 0)
        b9 = Tkinter.Button(text="Disburse", fg="black", command = disbursediag).grid(row = 8, column = 0)
        b10 = Tkinter.Button(text="Random", fg="black", command = randdiag).grid(row = 10, column = 0)
        b11 = Tkinter.Button(text="Seam Cut", fg="black", command = seamdiag).grid(row = 9, column = 0)
        seedlabel = Tkinter.Label(root, text = "Seed #: " + str(seed))
        seedlabel.grid(row = 13, column = 11, sticky = 'e')
        root.iconbitmap("@icon.xbm")
        root.mainloop()
    else:
        root.destroy()
        InvalidImageSize()
        startup()
    

def router():
    global picname
    global seed
    global im
    seed = None
    if not seed:
        try:
            seed = int(start.entry2.get())
            try :
                picname = str(start.entry1.get())
                im = Image.open(picname)
                print "Your seed was: " + str(seed)
                start.destroy()
                startit()
            except IOError:
                InvalidImage(start)
        except ValueError:
            InvalidSeed(start)

def opennew():
    root.destroy()
    startup()

def startup():
    global start
    global file
    
    start = Tkinter.Tk()
    start.title("Welcome, Friend!")
    start.resizable(0,0)
    Tkinter.Label(start, text="Filename:").pack(pady=5)
    start.entry1 = Tkinter.Entry(start)
    start.entry1.pack()

    def browse():
        file = str(tkFileDialog.askopenfilename(parent=start,title='Choose a file'))
        start.entry1.delete(0,9999999)
        start.entry1.insert(0, file)

    Tkinter.Button(start, text="Browse",command = browse).pack()

    Tkinter.Label(start, text="Seed:").pack( pady=5)
    start.entry2 = Tkinter.Entry(start)
    start.entry2.pack()

    def inputrand():
        start.entry2.delete(0,9999999)
        start.entry2.insert(0, random.randint(0,9999999))
        
    Tkinter.Button(start, text="Random Seed",command = inputrand).pack()


    button = Tkinter.Button(start, text="OK", command = router)
    button.pack(pady = 10)
    start.minsize(300,120)
    start.iconbitmap("@icon.xbm")
    start.mainloop()

startup()
