import getpass
import json
import os
import shutil
import smtplib
import sqlite3
import subprocess
import sys
import time
import webbrowser
from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

deps = Tk()

deps.title('Installation de modules...')


def installv():
    lblb.pack_forget()
    deps1 = LabelFrame(
        deps, text='Progression de l\'installation', padx=20, pady=20)
    deps1.pack()
    p = StringVar()
    p.set(0)
    pt = StringVar()
    p_l = Label(deps, textvariable=pt)
    p_l.pack()
    p_b = ttk.Progressbar(deps1, orient=HORIZONTAL,
                          length=500, mode='determinate', variable=p)
    p_b.pack()
    pt.set('Installation des modules pour le punchnox-project...')
    deps.update()
    subprocess.run('npm i discord.js@11.6.3', shell=True)
    p.set(5)
    deps.update()
    subprocess.run('pip install discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, datetime, smtplib, string, ctypes, webbrowser, discord, discord.ext, commands, os, requests, bs4, BeautifulSoup, json, random, time, asyncio, urlencode, cycle, Fore, gTTS', shell=True)
    p.set(9)
    deps.update()
    subprocess.run('npm i figlet', shell=True)
    p.set(10)
    deps.update()
    subprocess.run('npm i moment', shell=True)
    p.set(15)
    deps.update()
    subprocess.run('npm i colors', shell=True)
    p.set(20)
    deps.update()
    subprocess.run('npm i chance', shell=True)
    p.set(25)
    deps.update()
    subprocess.run('npm i math-expression-evaluator', shell=True)
    p.set(30)
    deps.update()
    subprocess.run('npm i base-64', shell=True)
    p.set(35)
    deps.update()
    subprocess.run('npm i fs', shell=True)
    p.set(40)
    deps.update()
    subprocess.run('npm i youtube-search', shell=True)
    p.set(45)
    deps.update()
    subprocess.run('npm i node-fetch', shell=True)
    p.set(50)
    deps.update()
    subprocess.run('npm i utf8', shell=True)
    p.set(55)
    deps.update()
    subprocess.run('npm i snekfetch', shell=True)
    p.set(60)
    deps.update()
    subprocess.run('npm i hastebin-gen', shell=True)
    p.set(65)
    deps.update()
    subprocess.run('npm i discordrpcgenerator', shell=True)
    p.set(70)
    deps.update()
    subprocess.run('npm i os', shell=True)
    p.set(75)
    deps.update()
    subprocess.run('npm i random-puppy', shell=True)
    p.set(80)
    deps.update()
    subprocess.run('npm i ms', shell=True)
    p.set(85)
    deps.update()
    subprocess.run('npm i @k3rn31p4nic/google-translate-api', shell=True)
    p.set(90)
    deps.update()
    subprocess.run('npm i child_process', shell=True)
    p.set(92)
    deps.update()
    subprocess.run('npm i weather-js', shell=True)
    p.set(94)
    deps.update()
    subprocess.run('npm i is-tuesday', shell=True)
    p.set(95)
    deps.update()
    subprocess.run('npm i https', shell=True)
    p.set(97)
    deps.update()
    subprocess.run('npm i amethyste-api', shell=True)
    p.set(98)
    deps.update()
    subprocess.run('npm i cpu-stat', shell=True)
    p.set(99)
    deps.update()
    subprocess.run('npm i discord.js-minesweeper', shell=True)
    p.set(100)
    deps.update()
    subprocess.run('npm i utils', shell=True)
    pt.set('Terminé.')
    deps.update()
    sys.exit()


lblb = Button(deps, text='installer', command=installv, width=30)
lblb.pack()

deps.mainloop()
