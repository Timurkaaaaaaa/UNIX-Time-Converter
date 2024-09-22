import customtkinter
from customtkinter import *
import datetime
from datetime import datetime
import time
import tkinter
import tkinter.messagebox
import pyperclip 
import config
import os
import sys
import io

cfg = config.Config("config.cfg")

app = customtkinter.CTk()
app.title("UNIX Конвертов")
app.geometry("720x450")
customtkinter.set_default_color_theme("dark-blue")
app.after(201, lambda :app.iconbitmap('assets/icon.ico'))
customtkinter.set_appearance_mode(cfg["appearance_mode"])
customtkinter.set_default_color_theme("themes/" + cfg["color_theme_path"])

def YearError():
    toplevel_window = None
    class ToplevelWindow(customtkinter.CTkToplevel):
      	def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("310x70")
            self.title("Ошибка")
            self.label = customtkinter.CTkLabel(self, text="Вы не можете указывать год ранее 1970!")
            self.label.pack(padx=20, pady=20)
    toplevel_window = ToplevelWindow()
    toplevel_window.focus()
    
def DayMonError():
    toplevel_window = None
    class ToplevelWindow(customtkinter.CTkToplevel):
      	def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("610x70")
            self.title("Ошибка")
            self.label = customtkinter.CTkLabel(self, text="Вы не можете указывать несуществующую дату!")
            self.label.pack(padx=20, pady=20)
    toplevel_window = ToplevelWindow()
    toplevel_window.focus()
    
def TimeError():
    toplevel_window = None
    class ToplevelWindow(customtkinter.CTkToplevel):
      	def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("610x70")
            self.title("Ошибка")
            self.label = customtkinter.CTkLabel(self, text="Вы не можете указывать несуществующее время!")
            self.label.pack(padx=20, pady=20)
    toplevel_window = ToplevelWindow()
    toplevel_window.focus()
    
def NullError():
    toplevel_window = None
    class ToplevelWindow(customtkinter.CTkToplevel):
      	def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("610x70")
            self.title("Ошибка")
            self.label = customtkinter.CTkLabel(self, text="Вы должны заполнить все поля!")
            self.label.pack(padx=20, pady=20)
    toplevel_window = ToplevelWindow()
    toplevel_window.focus()
    
def copy(a):
    pyperclip.copy(str(a))
    
def AnsDateToUnix(a):
    toplevel_window = None
    class ToplevelWindow(customtkinter.CTkToplevel):
      	def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("170x100")
            self.title("Результат")
            self.textbox = customtkinter.CTkTextbox(master=self, width=150, height=20, corner_radius=0)
            self.textbox.grid(row=0, column=1, sticky="n")
            self.textbox.insert("0.0", f"UNIX: {a}")
            self.button3 = customtkinter.CTkButton(master=self,width=150, height=20, text="Скопировать", command=copy(a))
            self.button3.grid(row=1, column=1, sticky="n")
    toplevel_window = ToplevelWindow()
    toplevel_window.focus()
    
def AnsUnixToDate(a):
    toplevel_window = None
    class ToplevelWindow(customtkinter.CTkToplevel):
      	def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("300x100")
            self.title("Результат")
            self.textbox = customtkinter.CTkTextbox(master=self, width=250, height=20, corner_radius=0)
            self.textbox.grid(row=0, column=1, sticky="n")
            self.textbox.insert("0.0", f"Дата и время: {a}")
            self.button3 = customtkinter.CTkButton(master=self,width=250, height=20, text="Скопировать", command=copy(a))
            self.button3.grid(row=1, column=1, sticky="n")
    toplevel_window = ToplevelWindow()
    toplevel_window.focus()
    
def date_to_unix():
    year = entry_year.get()+"0"
    mon = entry_mon.get()+"0"
    day = entry_day.get()+"0"
    hour = entry_hour.get()+"0"
    min = entry_min.get()+"0"
    sec = entry_sec.get()+"0"
    if(year!="0" and mon!="0" and day!="0" and hour!="0" and min!="0" and sec!="0"):
        year = int(year[:-1])
        mon = int(mon[:-1])
        day = int(day[:-1])
        hour = int(hour[:-1])
        min = int(min[:-1])
        sec = int(sec[:-1])
        toplevel_window = None
        if(year<1970):
              toplevel_window = None
              YearError()
        elif(mon>12 or day>31 or mon<0 or day<0):
              toplevel_window = None
              DayMonError()
        elif(hour>=24 or min>=60 or sec>=60 or hour<0 or min<0 or sec<0):
              toplevel_window = None
              TimeError()
        else:
              date_time = str(year) +"-"+ str(mon) +"-"+ str(day) +" "+ str(hour) +":"+ str(min) +":"+ str(sec)
              unixdatetime = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
              unixdatetime = unixdatetime.timestamp()
              unixdatetime = int(unixdatetime)
              AnsDateToUnix(unixdatetime)
    else:
        toplevel_window = None
        NullError()

def unix_to_date():
    unix = entry_unix.get()
    unix = float(unix)
    time_struct = time.gmtime(unix)
    a = time.strftime("%Y.%m.%d %H:%M:%S", time_struct)
    AnsUnixToDate(a)

datetounixFrame = customtkinter.CTkFrame(master=app, width=200, height=200)
datetounixFrame_var = tkinter.IntVar(value=0)
label_datetounixFrame = customtkinter.CTkLabel(master=datetounixFrame, text="В UNIX:")
label_datetounixFrame.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
entry_year = customtkinter.CTkEntry(master=datetounixFrame, placeholder_text="Введите год ...",  width=300, height=30)
entry_mon = customtkinter.CTkEntry(master=datetounixFrame, placeholder_text="Введите месяц ...",  width=300, height=30)
entry_day = customtkinter.CTkEntry(master=datetounixFrame, placeholder_text="Введите день ...",  width=300, height=30)
entry_hour = customtkinter.CTkEntry(master=datetounixFrame, placeholder_text="Введите час ...",  width=300, height=30)
entry_min = customtkinter.CTkEntry(master=datetounixFrame, placeholder_text="Введите минуту ...",  width=300, height=30)
entry_sec = customtkinter.CTkEntry(master=datetounixFrame, placeholder_text="Введите секунду ...",  width=300, height=30)
button1 = customtkinter.CTkButton(master=datetounixFrame, text="Конвертировать", command=date_to_unix, width=300, height=30) 

entry_year.grid(row=1, column=2, pady=10, padx=10, sticky="n")    
entry_mon.grid(row=2, column=2, pady=10, padx=10, sticky="n")    
entry_day.grid(row=3, column=2, pady=10, padx=10, sticky="n")    
entry_hour.grid(row=4, column=2, pady=10, padx=10, sticky="n")    
entry_min.grid(row=5, column=2, pady=10, padx=10, sticky="n")    
entry_sec.grid(row=6, column=2, pady=10, padx=10, sticky="n")
button1.grid(row=7, column=2, pady=10, padx=10, sticky="n")    
datetounixFrame.pack(padx=20, pady=20, side=LEFT)  

unixtodateFrame = customtkinter.CTkFrame(master=app, width=200, height=200)
unixtodateFrame_var = tkinter.IntVar(value=0)
label_unixtodateFrame = customtkinter.CTkLabel(master=unixtodateFrame, text="Из UNIX:")
label_unixtodateFrame.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
entry_unix = customtkinter.CTkEntry(master=unixtodateFrame, placeholder_text="Введите время в формате UNIX ...",  width=300, height=30)
entry_unix.grid(row=1, column=2, pady=10, padx=10, sticky="n")    
button2 = customtkinter.CTkButton(master=unixtodateFrame, text="Конвертировать", command=unix_to_date, width=300, height=30)
button2.grid(row=2, column=2, pady=10, padx=10, sticky="n")
unixtodateFrame.pack(padx=20, pady=20, side=RIGHT)  

app.mainloop()




