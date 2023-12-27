# from playsound import playsound
# playsound('29824782800192.mp3')

from tkinter import *
import tkSnack

root = Tk()
tkSnack.initializeSnack(root)

snd = tkSnack.Sound()
snd.read('Fashion1983.wav')
snd.play(blocking=1)