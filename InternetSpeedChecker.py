from tkinter import * 
from tkinter import messagebox
#pip install pyspeedtest
import pyspeedtest

def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+"[Bytes Per Second]")
    messagebox.showinfo("Your Download Speed: ", a1)

root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="blue")
root.geometry("500x250")

label1 = Label(root,text="Internet Speed Checker", font = ("Arial", 15, "bold"), bg= "lightblue").pack()
button1 = Button(root, text="Click", font=("Arial", 12, "bold"), bg="white", height=1, width=10, command=one).pack()

root.mainloop()