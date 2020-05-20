from tkinter import *
import os
import pygame
from tkinter import filedialog
import numpy as np
import pandas as pd

master = Tk()
master.minsize(360, 360)
master.title("mp3playerGUI")

trkno = 0
songs = []


def browse():
    global songs
    global dir
    songs = []
    dir = filedialog.askdirectory()
    os.chdir(dir)
    for i in os.listdir(dir):
        if i.endswith(".mp3"):
            songs.append(i)
    print
    songs
    pygame.mixer.init()
    pygame.mixer.music.load(songs[0])


a = np.zeros(56)
print
a

dir = filedialog.askdirectory()
os.chdir(dir)
for i in os.listdir(dir):
    if i.endswith(".mp3"):
        songs.append(i)
print
songs
pygame.mixer.init()
pygame.mixer.music.load(songs[0])


def play():
    global trkname
    global trkno
    global pi
    if pi == 0:
        pygame.mixer.music.play()
        trkname.set((str(songs[trkno])).replace(".mp3", ""))
    else:
        pygame.mixer.music.unpause()


def stop():
    global pi
    pygame.mixer.music.pause()
    pi = 1


def nexttrk():
    global trkname
    global trkno
    global songs
    trkno += 1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname.set((str(songs[trkno])).replace(".mp3", ""))


def prevtrk():
    global trkname
    global trkno
    global songs
    trkno -= 1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname.set((str(songs[trkno])).replace(".mp3", ""))


def voli():
    global vol
    vol = pygame.mixer.music.get_volume()
    vol += 0.1
    if vol >= 0.9921875:
        vol = 0.9921875
    pygame.mixer.music.set_volume(vol)


def vold():
    global vol
    vol = pygame.mixer.music.get_volume()
    vol -= 0.1
    if vol < 0:
        vol = 0.0
    pygame.mixer.music.set_volume(vol)


font1 = 'Calibri', 15, 'bold'
font2 = 'Calibri', 10, 'bold'

trkname = StringVar()
pi = 0
vol = 1
Label(master, text = 'You wanna hear some tunes?', font=font2).grid(row=1, column=4)
Button(master, text='>>|', command=nexttrk).grid(row=2, column=3, sticky=W, pady=4)
Button(master, text='|<<', command=prevtrk).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text='||', command=stop).grid(row=2, column=1, sticky=W, pady=4)
Button(master, text='>', command=play).grid(row=2, column=2, sticky=W, pady=4)
Label(master, textvariable=trkname, font=font1).grid(row=3, column=4)
Button(master, text=' + ', command=voli).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text=' - ', command=vold).grid(row=4, column=3, sticky=W, pady=4)
Button(master, text='Browse', command=browse).grid(row=4, column=4, sticky=W, pady=4)

master.mainloop()
