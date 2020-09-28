#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

def get_sum(event):
	Height = int(Height_Entry.get())
	Weight = int(Weight_Entry.get())
	Age = int(Age_Entry.get())
	sex_var = int(m_f.get())
	Exercise_fact = Exercise_factor.get()

	BMI_sum = round((100 * 100 * Weight) / (Height*Height))
	BMI_sumEntry.delete(0, "end")
	BMI_sumEntry.insert(0, BMI_sum)

	if sex_var == 1:
		BMR_sum = (66.5 + (13.75 * Weight) + (5.003 * Height) - (6.755 * Age))
	elif sex_var == 2:
		BMR_sum = (655.1 + (9.563 * Weight) + (1.850 * Height) - (4.676 * Age))

	BMR = round(BMR_sum)
	BMR_sumEntry.delete(0, "end")
	BMR_sumEntry.insert(0, BMR)

	TDEE_sum = round((float(BMR) * float(Exercise_fact)))
	TDEE_sumEntry.delete(0, "end")
	TDEE_sumEntry.insert(0, TDEE_sum)

root = Tk()
root.title("BMI / BMR / TDEE Calculator v0.1")

Height_Label = Label(root, text="Enter Height (in CM): ").grid(row=0, column=0, sticky=W)
Height_Entry = Entry(root)
Height_Entry.grid(row=0, column=1)

Weight_Label = Label(root, text="Enter Weight (in KG): ").grid(row=1, column=0, sticky=W)
Weight_Entry = Entry(root)
Weight_Entry.grid(row=1, column=1)

Age_Label = Label(root, text="Enter age: ").grid(row=2, column=0, sticky=W)
Age_Entry = Entry(root)
Age_Entry.grid(row=2, column=1)

m_f = IntVar()
Radio_label = Label(root, text="What is your sex: ").grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Male", variable=m_f, value=1).grid(row=3, column=1, sticky=W)
Radiobutton(root, text="Female", variable=m_f, value=2).grid(row=3, column=2, sticky=NW)

Exercise_factor = StringVar()
Radio_label = Label(root, text="How active are you?").grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Sedentary", variable=Exercise_factor, value=1.2).grid(row=4, column=1, sticky=W)
Radiobutton(root, text="Lightly active", variable=Exercise_factor, value=1.375).grid(row=5, column=1, sticky=W)
Radiobutton(root, text="Moderately active", variable=Exercise_factor, value=1.55).grid(row=6, column=1, sticky=W)
Radiobutton(root, text="Very active", variable=Exercise_factor, value=1.725).grid(row=7, column=1, sticky=W)
Radiobutton(root, text="Extra active", variable=Exercise_factor, value=1.9).grid(row=8, column=1, sticky=W)

submit_Button = Button(root, text="Calculate BMI and BMR")
submit_Button.bind("<Button-1>", get_sum)
submit_Button.grid(row=9, column=1)

BMI_SumLabel = Label(root, text="Your BMI is: ").grid(row=10, column=0, sticky=W)
BMI_sumEntry = Entry(root)
BMI_sumEntry.grid(row=10, column=1)

BMR_SumLabel = Label(root, text="Your BMR is: ").grid(row=11, column=0, sticky=W)
BMR_sumEntry = Entry(root)
BMR_sumEntry.grid(row=11, column=1)

TDEE_SumLabel = Label(root, text="Your TDEE is: ").grid(row=12, column=0, sticky=W)
TDEE_sumEntry = Entry(root)
TDEE_sumEntry.grid(row=12, column=1)

root.mainloop()
