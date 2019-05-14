from tkinter import *
import re
import reg_ex

master = Tk()

def check(arg=None):
	valider(e1.get(), reg_ex.navn, l1)
	valider(e2.get(), reg_ex.adresse, l2)
	valider(e3.get(), reg_ex.postnummer, l3)
	valider(e4.get(), reg_ex.by, l4)
	valider(e5.get(), reg_ex.mobil, l5)
	valider(e6.get(), reg_ex.email, l6)
	valider(e7.get(), reg_ex.fodselsdag, l7)

def valider(streng, reg, label):
	pattern = re.compile(reg)
	if pattern.match(streng):
	    label.config(text='OK', fg = "green")
	else:
	    label.config(text='Ej OK', fg = "red")

def slet():
	e1.delete(0,"end")
	e2.delete(0,"end")
	e3.delete(0,"end")
	e4.delete(0,"end")
	e5.delete(0,"end")
	e6.delete(0,"end")
	e7.delete(0,"end")

Label(master, text="Fulde navn:").grid(row=0, sticky = W)
Label(master, text="Adresse:").grid(row=1, sticky = W)
Label(master, text="Postnummer:").grid(row=2, sticky = W)
Label(master, text="By:").grid(row=3, sticky = W)
Label(master, text="Mobil:").grid(row=4, sticky = W)
Label(master, text="email:").grid(row=5, sticky = W)
Label(master, text="Fodselsdag:").grid(row=6, sticky = W)

l1 = Label(master, text="  ")
l2 = Label(master, text="  ")
l3 = Label(master, text="  ")
l4 = Label(master, text="  ")
l5 = Label(master, text="  ")
l6 = Label(master, text="  ")
l7 = Label(master, text="  ")

l1.grid(row=0, column=2)
l2.grid(row=1, column=2)
l3.grid(row=2, column=2)
l4.grid(row=3, column=2)
l5.grid(row=4, column=2)
l6.grid(row=5, column=2)
l7.grid(row=6, column=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

Button(master, text='Annuller', command=slet).grid(row=8, column=1, sticky=W, pady=4)
Button(master, text='Godkend', command=check).grid(row=8, column=1, sticky=E, pady=4)

master.bind("<Return>", check)
mainloop()
