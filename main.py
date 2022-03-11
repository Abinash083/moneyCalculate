from tkinter import *

exchange_rate = 90

def convert():
    value_in_Aud = float(aud_box.get())
    value_in_Nrp = float(aud_box.get())
    if value_in_Aud != 0.0:
        value_in_Nrp = value_in_Aud * exchange_rate
        nrp_box.delete(0, END)
        nrp_box.insert(0, f"{value_in_Nrp}")
    elif value_in_Nrp != 0.0:
        value_in_Aud = value_in_Nrp / exchange_rate
        aud_box.delete(0, END)
        aud_box.insert(0, f"{value_in_Aud}")



window = Tk()
window.title("Unit changing")
window.minsize()
window.config(padx=30, pady=20)
unit_label = Label(text="AUD TO NRP")
unit_label.grid(column=1, row=0)
Aud_label = Label(text="AUD")
Aud_label.grid(column=0, row=1)
Nrp_label = Label(text="NRP")
Nrp_label.grid(column=2, row=1)

value_in_Aud = 0
value_in_Nrp = 0

aud_box = Entry()
aud_box.focus()
aud_box.grid(column=0, row=2)

arrow_label = Label(text="⇋", font=("Arial", 20))
arrow_label.grid(column=1, row=2)

nrp_box = Entry()
nrp_box.grid(column=2, row=2)

con_button = Button(text="Convert", command=convert)
con_button.grid(column=1, row=3)

window.mainloop()
