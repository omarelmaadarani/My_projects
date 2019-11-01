import json
from difflib import get_close_matches
from tkinter import *

data = json.load(open("data.json"))

window = Tk()

def yes_no():
    if z.get() == "yes":
        t1.delete("1.0", END)
        t1.insert(END,data[get_close_matches(w.get(),data.keys())[0]])
    elif z.get() == "no":
        t1.delete("1.0", END)
        t1.insert(END,"The word doesn't exist please double check it")
    else:
        t1.delete("1.0", END)
        t1.insert(END,"We didn't understand your entry")

def translate():
    c = w.get().lower()
    if c in data:
        t1.delete("1.0", END)
        t1.insert(END,data[c])
    elif c.title() in data:
        t1.delete("1.0", END)
        t1.insert(END,data[c.title()])
    elif c.upper() in data:
        t1.delete("1.0", END)
        t1.insert(END,data[c.upper()])
    elif len(get_close_matches(c,data.keys())) > 0:
        t2.delete("1.0", END)
        t2.insert(END,"DO you mean %s instead, if Yes enter yes, if No enter no" %get_close_matches(c,data.keys())[0])
    else:
        v = "The word doesn't exist please double check it"
        t1.delete("1.0", END)
        t1.insert(END,str(v))

b1 = Button(window,text="Execute",command=translate)
b1.grid(row=0,column=0)

b2 = Button(window,text="Yes/NO",command=yes_no)
b2.grid(row=0,column=3)

w = StringVar()
e1=Entry(window,textvariable = w)
e1.grid(row=0,column=1)

z = StringVar()
e2=Entry(window,textvariable = z)
e2.grid(row=0,column=4)

t1=Text(window)
t1.grid(row=1,column=2)

t2=Text(window,height =1,width=70)
t2.grid(row=0,column=2)

window.mainloop()
