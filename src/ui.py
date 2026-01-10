import tkinter as tk
from tkinter import ttk
import os
import csv
import time
import datetime
from .logic import take_images, train_images, track_images
from .auth import change_pass, psw_check

class AttendanceSystemApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1280x720")
        self.window.resizable(True, False)
        self.window.title("GEC JAGDALPUR Attendance System")
        self.window.configure(background='#262523')
        
        self.mont = {
            '01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
            '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'
        }
        
        self.setup_ui()
        self.update_registrations_count()
        self.tick()

    def tick(self):
        time_string = time.strftime('%H:%M:%S')
        self.clock.config(text=time_string)
        self.clock.after(200, self.tick)

    def setup_ui(self):
        self.frame1 = tk.Frame(self.window, bg="#00aeff")
        self.frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

        self.frame2 = tk.Frame(self.window, bg="#00aeff")
        self.frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

        tk.Label(self.window, text="Face Recognition Based Attendance System", fg="white", bg="#262523", width=55, height=1, font=('times', 29, ' bold ')).place(x=10, y=10)

        frame3 = tk.Frame(self.window, bg="#c4c6ce")
        frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)
        frame4 = tk.Frame(self.window, bg="#c4c6ce")
        frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        day, month, year = date.split("-")
        
        tk.Label(frame4, text=f"{day}-{self.mont[month]}-{year} | ", fg="orange", bg="#262523", width=50, height=1, font=('times', 17, ' bold ')).pack(fill='both', expand=1)
        self.clock = tk.Label(frame3, fg="orange", bg="#262523", width=55, height=1, font=('times', 19, ' bold '))
        self.clock.pack(fill='both', expand=1)

        tk.Label(self.frame2, text=" For New Registrations ", fg="black", bg="#3ece48", font=('times', 17, ' bold ')).grid(row=0, column=0)
        tk.Label(self.frame1, text=" For Already Registered ", fg="black", bg="#3ece48", font=('times', 17, ' bold ')).place(x=0, y=0)

        tk.Label(self.frame2, text="Enter Roll Number", width=20, height=1, fg="black", bg="#00aeff", font=('times', 17, ' bold ')).place(x=80, y=55)
        self.txt_roll = tk.Entry(self.frame2, width=32, fg="black", font=('times', 15, ' bold '))
        self.txt_roll.place(x=30, y=88)

        tk.Label(self.frame2, text="Enter Name", width=20, fg="black", bg="#00aeff", font=('times', 17, ' bold ')).place(x=80, y=140)
        self.txt_name = tk.Entry(self.frame2, width=32, fg="black", font=('times', 15, ' bold '))
        self.txt_name.place(x=30, y=173)

        self.message1 = tk.Label(self.frame2, text="1)Take Images >>> 2)Save Profile", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 15, ' bold '))
        self.message1.place(x=7, y=230)

        self.message = tk.Label(self.frame2, text="", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 16, ' bold '))
        self.message.place(x=7, y=450)

        tk.Label(self.frame1, text="Attendance", width=20, fg="black", bg="#00aeff", height=1, font=('times', 17, ' bold ')).place(x=100, y=115)

        menubar = tk.Menu(self.window, relief='ridge')
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Change Password', command=change_pass)
        filemenu.add_command(label='Contact Us', command=self.contact)
        filemenu.add_command(label='Exit', command=self.window.destroy)
        menubar.add_cascade(label='Help', font=('times', 29, ' bold '), menu=filemenu)
        self.window.configure(menu=menubar)

        self.tv = ttk.Treeview(self.frame1, height=13, columns=('name', 'date', 'time'))
        self.tv.column('#0', width=82)
        self.tv.column('name', width=130)
        self.tv.column('date', width=133)
        self.tv.column('time', width=133)
        self.tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
        self.tv.heading('#0', text='ID')
        self.tv.heading('name', text='NAME')
        self.tv.heading('date', text='DATE')
        self.tv.heading('time', text='TIME')

        scroll = ttk.Scrollbar(self.frame1, orient='vertical', command=self.tv.yview)
        scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
        self.tv.configure(yscrollcommand=scroll.set)

        tk.Button(self.frame2, text="Clear", command=self.clear_roll, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold ')).place(x=335, y=86)
        tk.Button(self.frame2, text="Clear", command=self.clear_name, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold ')).place(x=335, y=172)
        tk.Button(self.frame2, text="Take Images", command=self.take_step, fg="white", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, ' bold ')).place(x=30, y=300)
        tk.Button(self.frame2, text="Save Profile", command=self.save_step, fg="white", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, ' bold ')).place(x=30, y=380)
        tk.Button(self.frame1, text="Take Attendance", command=self.track_step, fg="black", bg="yellow", width=35, height=1, activebackground="white", font=('times', 15, ' bold ')).place(x=30, y=50)
        tk.Button(self.frame1, text="Quit", command=self.window.destroy, fg="black", bg="red", width=35, height=1, activebackground="white", font=('times', 15, ' bold ')).place(x=30, y=450)

    def clear_roll(self):
        self.txt_roll.delete(0, 'end')
        self.message1.configure(text="1)Take Images >>> 2)Save Profile")

    def clear_name(self):
        self.txt_name.delete(0, 'end')
        self.message1.configure(text="1)Take Images >>> 2)Save Profile")

    def take_step(self):
        take_images(self.txt_roll, self.txt_name, self.message1, self.message, self.window)

    def save_step(self):
        psw_check(lambda: train_images(self.message1, self.message, self.window))

    def track_step(self):
        track_images(self.tv, self.window)

    def contact(self):
        from tkinter import messagebox as mess
        mess._show(title='Contact us', message="Please contact us on : 'girishkumargupta11@gmail.com'")

    def update_registrations_count(self):
        res = 0
        exists = os.path.isfile("StudentDetails\\StudentDetails.csv")
        if exists:
            with open("StudentDetails\\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for _ in reader1:
                    res += 1
            res = (res // 2) - 1
        self.message.configure(text=f'Total Registrations till now : {res}')
