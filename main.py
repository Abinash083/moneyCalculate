from tkinter import *

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
aud_box.insert(END, string=f"{value_in_Aud}")
aud_box.focus()
value_in_Aud = aud_box.get()
aud_box.grid(column=0, row=2)

arrow_label = Label(text="⇋", font=("Arial", 20))
arrow_label.grid(column=1, row=2)

nrp_box = Entry()
nrp_box.insert(END, string=f"{value_in_Nrp}")
value_in_Nrp = aud_box.get()
nrp_box.grid(column=2, row=2)

con_button = Button(text="Convert")
con_button.grid(column=1, row=3)

window.mainloop()
