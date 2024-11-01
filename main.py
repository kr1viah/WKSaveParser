from tkinter import *
import os
import json
import tkinter
from tkinter import font as tkFont
appdata_path = os.getenv("APPDATA")

file_path = os.path.join(appdata_path, "Godot/app_userdata/windowkill", "stats.res")

def readFile(file):
    data = json.load(file)
    thismetaStats = data.get("metaStats", [])
    for stat in thismetaStats:
        metaStatsName.append(stat)
        metaStatsItem.append(thismetaStats.get(stat, []))

metaStatsName = []
metaStatsItem = []
try:
    with open(file_path, "r") as file:
        readFile(file)
except FileNotFoundError:
    print("file not found")
except json.JSONDecodeError:
    print("wtf is wrong with your save")

win = Tk()

font = tkFont.Font(family="Lucida Console", size=12)

win.title("Windowkill save parser")
win.geometry("505x800")
win.config(bg="lightblue")
win.iconbitmap("icon.ico")
win.resizable(False, False)

metaStatsListBox = Listbox(win, font=font, width=50, height=15, takefocus=0, disabledforeground="black")
metaStatsListBox.pack(fill=X, expand=True, side=LEFT)
metaStatsListBox.place(x=0, y=15)
for item in range(len(metaStatsName)):
    amountOfWhiteSpace = 25 - len(metaStatsName[item])
    thingToBeInserted = metaStatsName[item]+":"
    for i in range(amountOfWhiteSpace):
        thingToBeInserted += " "
    thingToBeInserted += str(metaStatsItem[item])
    metaStatsListBox.insert(END, thingToBeInserted)

metaStatsListBox.config(state='disabled')

win.mainloop()