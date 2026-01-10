import os
from tkinter import messagebox as mess

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def check_haarcascadefile(window):
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        return True
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()
        return False
