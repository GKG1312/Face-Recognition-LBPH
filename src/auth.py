import os
import tkinter as tk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
from .utils import assure_path_exists

def save_pass(master, old_entry, new_entry, nnew_entry):
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\\psd.txt")
    if exists1:
        with open("TrainingImageLabel\\psd.txt", "r") as tf:
            key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas is None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
            return
        else:
            with open("TrainingImageLabel\\psd.txt", "w") as tf:
                tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = old_entry.get()
    newp = new_entry.get()
    nnewp = nnew_entry.get()
    if op == key:
        if newp == nnewp:
            with open("TrainingImageLabel\\psd.txt", "w") as txf:
                txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

def change_pass():
    master = tk.Toplevel()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    
    tk.Label(master, text=' Enter Old Password', bg='white', font=('times', 12, ' bold ')).place(x=10, y=10)
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    
    tk.Label(master, text=' Enter New Password', bg='white', font=('times', 12, ' bold ')).place(x=10, y=45)
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    
    tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold ')).place(x=10, y=80)
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    
    tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25, activebackground="white", font=('times', 10, ' bold ')).place(x=200, y=120)
    tk.Button(master, text="Save", command=lambda: save_pass(master, old, new, nnew), fg="black", bg="#3ece48", height=1, width=25, activebackground="white", font=('times', 10, ' bold ')).place(x=10, y=120)

def psw_check(on_success):
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\\psd.txt")
    if exists1:
        with open("TrainingImageLabel\\psd.txt", "r") as tf:
            key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas is None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
            return
        else:
            with open("TrainingImageLabel\\psd.txt", "w") as tf:
                tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if password == key:
        on_success()
    elif password is None:
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')
