from tkinter import *

# Widget that will convert miles into kilometers
window1 = Tk()

def km_miles():
    text1.delete(1.0,END)
    print(entry1_value.get())
    miles = float(entry1_value.get())/1.6
    text1.insert(END, miles)


b1 = Button(window1, text="Execute", command=km_miles)
b1.grid(row=0, column=0, rowspan=2)

entry1_value = StringVar()
entry1 = Entry(window1, textvariable=entry1_value)
entry1.grid(row=0, column=1)

text1 = Text(window1, height=2, width=20)
text1.grid(row=0, column=2)

window1.mainloop()

# Widget that will convert kilograms into other units
win2 = Tk()

def conversion():
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    t4.delete(1.0, END)
    grams = float(e2_value.get())*1000
    pounds = float(e2_value.get())*2.205
    ounces = float(e2_value.get())*35.274
    t2.insert(END, grams)
    t3.insert(END, pounds)
    t4.insert(END, ounces)


l2 = Label(win2, text="Kg", width=25, pady=2, bg="gray")
l2.grid(row=0, column = 0)

e2_value = StringVar()
e2 = Entry(win2, textvariable=e2_value)
e2.grid(row=0, column=1)

b2 = Button(win2, text="Convert!!", width=25, command=conversion)
b2.grid(row=0, column=2)

t2 = Text(win2, height=1, width=25)
t2.grid(row=1, column=0)

t3 = Text(win2, height=1, width=25)
t3.grid(row=1, column=1)

t4 = Text(win2, height=1, width=25)
t4.grid(row=1, column=2)

win2.mainloop()
