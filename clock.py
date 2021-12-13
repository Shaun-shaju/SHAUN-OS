from tkinter import *
from tkinter.ttk import *
from time import strftime

app = Tk()
app.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(app, font= ("DS-Digital Bold Italic", 80), background='blue', foreground='pink')
label.pack(anchor='center')
time()

mainloop()