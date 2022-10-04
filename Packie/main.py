import os
import modules
import json

from tkinter import *

win = Tk()
win.title('Packie')
win.geometry('620x340+0+0')
win.wm_iconphoto(True, PhotoImage(file='packie.png'))
win.configure(bg='#34abeb')

TXT = Label(win, text='PACKIE')
TXT.configure()
TXT.place(x=320, y=60)

def upload(name, user, passw): 
    try:
        modules.modules.uploader.upload(name, user, passw)
        TXT.configure(text='Uploading DONE!', fg='#02f01a')
    except:
        TXT.configure(text='Uploading Failed', fg='#ed0c00')
    
def package(loc, username, password, name, vers, auth, home, bug, email, smdes, lrgdes, _repack_): 
    try:
        modules.modules.packager.pack(loc, smdes, auth, name, vers, home, bug, email, lrgdes, _repack_)
        TXT.configure(text='Packaging DONE!', fg='#02f01a')
    except:
        TXT.configure(text='Packaging Failed', fg='#ed0c00')
    
PKGNAME = Entry(win, text='Package Name')
PKGNAME.insert(10, 'Package Name')
PKGNAME.place(x=90, y=20)

PKAUTHR = Entry(win, text='Package Author')
PKAUTHR.insert(10, 'Package Author')
PKAUTHR.place(x=90, y=40)

PKVERSN = Entry(win, text='Package Version')
PKVERSN.insert(10, 'Package Version')
PKVERSN.place(x=90, y=60)

PKHMPGE = Entry(win, text='Package Homepage')
PKHMPGE.insert(10, 'Package Homepage')
PKHMPGE.place(x=90, y=80)

PKBUGPG = Entry(win, text='Package Bugpage')
PKBUGPG.insert(10, 'Package Bugpage')
PKBUGPG.place(x=90, y=100)

PKEMAIL = Entry(win, text='Package Email')
PKEMAIL.insert(10, 'Package Email')
PKEMAIL.place(x=90, y=120)

PKSMDES = Entry(win, text='Small Description')
PKSMDES.insert(10, 'Small Description')
PKSMDES.place(x=90, y=140)

PKLRGDS = Entry(win, text='Large Description')
PKLRGDS.insert(10, 'Description')
PKLRGDS.place(x=90, y=160)

PKLOCAT = Entry(win, text='Package Location')
PKLOCAT.insert(10, 'Package Location')
PKLOCAT.place(x=90, y=180)

PKUSERN = Entry(win, text='Username')
PKUSERN.insert(10, 'Username')
PKUSERN.place(x=90, y=200)

PKPASSW = Entry(win, text='Password', show='*')
PKPASSW.insert(10, 'Password')
PKPASSW.place(x=90, y=220)

def pac():
    TXT.configure(text='Packaging...', fg='#1e0557')
    package(PKLOCAT.get(), PKUSERN.get(), PKPASSW.get(), PKGNAME.get(), PKVERSN.get(), PKAUTHR.get(), PKHMPGE.get(), PKBUGPG.get(), PKEMAIL.get(), PKSMDES.get(), PKLRGDS.get(), False)

def rpac():
    TXT.configure(text='Repackaging...', fg='#1e0557')
    package(PKLOCAT.get(), PKUSERN.get(), PKPASSW.get(), PKGNAME.get(), PKVERSN.get(), PKAUTHR.get(), PKHMPGE.get(), PKBUGPG.get(), PKEMAIL.get(), PKSMDES.get(), PKLRGDS.get(), True)

def up():
    TXT.configure(text='Uploading...', fg='#1e0557')
    upload(PKGNAME.get(), PKUSERN.get(), PKPASSW.get())

def save():
    f = open('preset.json', 'r')
    JSFL = json.load(f)
    f.close()

    f = open('preset.json', 'w+')
    
    JSFL['preset']['pack_name'] = PKGNAME.get()
    JSFL['preset']['pack_auth'] = PKAUTHR.get()
    JSFL['preset']['pack_vers'] = PKVERSN.get()
    JSFL['preset']['pack_home'] = PKHMPGE.get()
    JSFL['preset']['pack_bugp'] = PKBUGPG.get()
    JSFL['preset']['pack_emal'] = PKEMAIL.get()
    JSFL['preset']['pack_smds'] = PKSMDES.get()
    JSFL['preset']['pack_desc'] = PKLRGDS.get()
    JSFL['preset']['pack_loca'] = PKLOCAT.get()
    JSFL['preset']['pack_user'] = PKUSERN.get()
    JSFL['preset']['pack_pass'] = PKPASSW.get()

    json.dump(JSFL, f)
    f.close()

def load():
    f = open('preset.json', 'r')
    JSFL = json.load(f)
    f.close()

    PKGNAME.delete(first=0, last=999)
    PKAUTHR.delete(first=0, last=999)
    PKVERSN.delete(first=0, last=999)
    PKHMPGE.delete(first=0, last=999)
    PKBUGPG.delete(first=0, last=999)
    PKEMAIL.delete(first=0, last=999)
    PKSMDES.delete(first=0, last=999)
    PKLRGDS.delete(first=0, last=999)
    PKLOCAT.delete(first=0, last=999)
    PKUSERN.delete(first=0, last=999)
    PKPASSW.delete(first=0, last=999)

    PKGNAME.insert(10, JSFL['preset']['pack_name'])
    PKAUTHR.insert(10, JSFL['preset']['pack_auth'])
    PKVERSN.insert(10, JSFL['preset']['pack_vers'])
    PKHMPGE.insert(10, JSFL['preset']['pack_home'])
    PKBUGPG.insert(10, JSFL['preset']['pack_bugp'])
    PKEMAIL.insert(10, JSFL['preset']['pack_emal'])
    PKSMDES.insert(10, JSFL['preset']['pack_smds'])
    PKLRGDS.insert(10, JSFL['preset']['pack_desc'])
    PKLOCAT.insert(10, JSFL['preset']['pack_loca'])
    PKUSERN.insert(10, JSFL['preset']['pack_user'])
    PKPASSW.insert(10, JSFL['preset']['pack_pass'])

PKG = Button(win, text='Package', command=pac)
PKG.configure(bg='#345eeb', width=9, height=2)
PKG.place(x=3, y=60)

RPK = Button(win, text='Re-pack', command=rpac)
RPK.configure(bg='#345eeb', width=9, height=2)
RPK.place(x=3, y=110)

UPL = Button(win, text='Upload', command=up)
UPL.configure(bg='#345eeb', width=9, height=2)
UPL.place(x=3, y=10)

SVP = Button(win, text='Save Preset', command=save)
SVP.configure(bg='#345eeb', width=9, height=2)
SVP.place(x=3, y=160)

LDP = Button(win, text='Load Preset', command=load)
LDP.configure(bg='#345eeb', width=9, height=2)
LDP.place(x=3, y=210)








win.mainloop()