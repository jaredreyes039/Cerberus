#!/bin/python

import tkinter as tk


window = tk.Tk()
window.config(cursor='', background='#000000')
window.geometry('500x750')
window.resizable(False, False)
window.title("Cerberus v3.0")

keycount = 0
passcount = 0
# Headers

header = tk.Label(
    window, 
    text="Cerberus v3.0",
    background="#000000",
    foreground='#ffffff',
    font=('monospace 25'),
    padx=5,
    pady=10,
    underline=9,
    )
subheader = tk.Label(
    window, 
    text="Passwords managed by Hell's finest!",
    background="#000000",
    foreground='#e90021',
    font=('monospace 14'),
    padx=5,
    pady=10,
    )

# Main GUI

keylbl = tk.Label(
    window,
    background='#000000',
    foreground='#ffffff',
    text="Enter Key File Name:",
        font='monospace 14'
)

keyinp = tk.Entry(
    window,
    width = 50,
    background='#000000',
    foreground='#ffffff',
    )
passlbl = tk.Label(
    window,
    background='#000000',
    foreground='#ffffff',
    text="Enter Hell File Name:",
        font='monospace 14'
)

passinp = tk.Entry(
    window,
    width = 50,
    background='#000000',
    foreground='#ffffff',
    )
reqpasslbl = tk.Label(
    window,
    background='#000000',
    foreground='#ffffff',
    text="Enter Password Name:",
    font='monospace 14'
)

reqpassinp = tk.Entry(
    window,
    width = 50,
    background='#000000',
    foreground='#ffffff',
    )

# Functions

# Click Handlers


def onClick():
    global keycount
    path_key = keyinp.get()
    if keycount == 0:
        myLabel = tk.Label(window, text="Path: " + str(path_key))
        myLabel.pack()
        passlbl.pack(ipadx=5,ipady=5,padx=5,pady=5)
        passinp.pack(ipady=5, ipadx=5, padx=10, pady=10)
        passbtn.pack(ipadx=0,ipady=0,anchor='center', padx=10, pady=10)
    else:
        myLabel = tk.Label(window, text="Path: " + str(path_key))
        myLabel.pack()
    keycount += 1

def onClickpass():
    global passcount
    path_pass = passinp.get()
    if passcount == 0:
        myLabel = tk.Label(window, text="Path: " + str(path_pass))
        myLabel.pack()
        reqpasslbl.pack(ipadx=5,ipady=5,padx=5,pady=5)
        reqpassinp.pack(ipady=5, ipadx=5, padx=10, pady=10)
        reqpassbtn.pack(ipadx=0,ipady=0,anchor='center', padx=10, pady=10)
    else:
        myLabel = tk.Label(window, text="Path: " + str(path_pass))
        myLabel.pack()
    passcount += 1

def onClickreq():
    req = reqpassinp.get()
    myLabel = tk.Label(window, text="Password: " + str(req))
    myLabel.pack()
    exitbtn.pack(ipadx=0,ipady=0,anchor='center', padx=30, pady=30)

def onClickExit():
    window.destroy()
# Encryption Handlers



# GUI Buttons

keybtn = tk.Button(window,
                text= "Get Key",
                padx=5,
                pady=2,
                background='#333333',
                foreground='#ffffff',
                command=onClick
)

passbtn = tk.Button(window,
                text= "Get Hell File",
                padx=5,
                pady=2,
                background='#333333',
                foreground='#ffffff',
                command=onClickpass
)
reqpassbtn = tk.Button(window,
                text= "Get Password",
                padx=5,
                pady=2,
                background='#333333',
                foreground='#ffffff',
                command=onClickreq
)
exitbtn = tk.Button(
    window, 
    text="Leave Hell (for now...)", 
    command=onClickExit,
    padx=5,
    pady=2,
    background='#333333',
    foreground='#ffffff'
)
# Format

header.pack(ipadx=0, ipady=0, fill=tk.X)
subheader.pack(ipadx=0,ipady=5,fill=tk.X)

keylbl.pack(ipadx=5,ipady=5,padx=5,pady=5)
keyinp.pack(ipady=5, ipadx=5, padx=10, pady=10)
keybtn.pack(ipadx=0,ipady=0,anchor='center', padx=10, pady=10)


# BP

window.mainloop()