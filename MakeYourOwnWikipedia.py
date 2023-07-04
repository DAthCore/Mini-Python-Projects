#pip install wikipedia
import tkinter
from tkinter  import *
import wikipedia as wk

window = Tk()
window.title("My Own Mini-Wikipedia")
window.config(bg="black")
f1_heading = Frame(window)
f2_frame = Frame(window)
f3_result = Frame(window)

Label(f1_heading, text="My Own Mini-Wikipedia", font=("Times", 30, "bold"), bg="lightblue").pack(side=TOP)
Label(f2_frame, text="Search Here:", font=("Arial", 20, "bold"), bg="white").pack(side=LEFT)
Label(f3_result, text="Searched Results:", font=("Arial", 25, "bold"), bg="green").pack(side=LEFT)

entry_box = Entry(f2_frame, width=40, font=("Arial", 20, "bold"))
entry_box.pack(side=LEFT, fill=BOTH, expand=5)
entry_box.focus_set()

query = ''
text = Text(window, font=("Times", 15, "bold"), bg="lightblue", padx=55, pady=10)

def textSearch():
    global query
    query = entry_box.get()
    try:
        textSumary = wk.summary(query)
        text.insert('1.0', textSumary)
    except:
        text.insert('1.0', 'No Results Found')

button1 = Button(f2_frame, text="Search", command=textSearch, font=("Arial", 15, "bold"), bg="gray", fg="white")
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP, pady=20, padx=50)
text.pack()


window.mainloop()