"""
Python Audio Project

Mixer Documentation(https://ww.pygame.org/docs/ref/mixcer.html)

Key Press Documentation (https://pygame.org/docs/ref/key.html)

"""

#Import modules
import pygame
import tkinter as tkr
import os


#Create Window
player = tkr.Tk()

#Edit Window
player.title("Audio Player")
player.geometry("205x340")

#player register path
os.chdir(r"D:\songs")
songlist = os.listdir()

#Volume Controls
VolumeLevel = tkr.Scale(player, from_=0.0, to_=1.0, orient = tkr.HORIZONTAL, resolution = 0.1)

#Playlist
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#Pygame inits
pygame.init()
pygame.mixer.init()

#Action Event 
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())


def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()


#Buttons
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command= Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=Pause)
button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=UnPause)


#Song Name 
#label1 = tkr.LabelFrame(player, text="Song Name")
#label1.pack(fill="both", expand="yes")
#contents1 = tkr.Label(label1, text = file)
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)


#Place Widgets
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
songtitle.pack()
VolumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")



#Activate (run program)
player.mainloop()

