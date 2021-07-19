from tkinter import Tk, Label, Radiobutton, Entry, IntVar, StringVar, Button

def get_sum(event):
	# Reset values so we can restart our calculations
	BMI_sumEntry.delete(0, "end")
	BMR_sumEntry.delete(0, "end")
	TDEE_sumEntry.delete(0, "end")

	# Get information from table
	Height = float(Height_Entry.get().replace(",", "."))
	Weight = float(Weight_Entry.get().replace(",", "."))
	Age = int(Age_Entry.get())
	sex_var = int(m_f.get())
	Exercise_fact = Exercise_factor.get()

	# Calculate the BMI
	BMI_sum = round((100 * 100 * Weight) / (Height*Height))
	BMI_sumEntry.insert(0, BMI_sum)

	# Calculate BMR, basex on the sex selecation
	if sex_var == 1:
		BMR_sum = (66.5 + (13.75 * Weight) + (5.003 * Height) - (6.755 * Age))
	elif sex_var == 2:
		BMR_sum = (655.1 + (9.563 * Weight) + (1.850 * Height) - (4.676 * Age))
	BMR_sumEntry.insert(0, BMR_sum)

	# Calculate the TDEE values
	TDEE_sum = round((float(BMR_sum) * float(Exercise_fact)))
	TDEE_sumEntry.insert(0, TDEE_sum)

# Start the tkinter screen
root = Tk()

root.title("BMI / BMR / TDEE Calculator v0.1")

Label(root, text="Enter Height (in CM): ").grid(row=0, column=0, sticky='W')
Height_Entry = Entry(root)
Height_Entry.grid(row=0, column=1)

Label(root, text="Enter Weight (in KG): ").grid(row=1, column=0, sticky='W')
Weight_Entry = Entry(root)
Weight_Entry.grid(row=1, column=1)

Label(root, text="Enter age: ").grid(row=2, column=0, sticky='W')
Age_Entry = Entry(root)
Age_Entry.grid(row=2, column=1)

m_f = IntVar()
Label(root, text="What is your sex: ").grid(row=3, column=0, sticky='W')
Radiobutton(root, text="Male", variable=m_f, value=1).grid(row=3, column=1, sticky='W')
Radiobutton(root, text="Female", variable=m_f, value=2).grid(row=3, column=2, sticky='NW')

Exercise_factor = StringVar(value="1")
Label(root, text="How active are you?").grid(row=4, column=0, sticky='W')
Radiobutton(root, text="Sedentary", variable=Exercise_factor, value=1.2).grid(row=5, column=0, sticky='W')
Radiobutton(root, text="Lightly active", variable=Exercise_factor, value=1.375).grid(row=5, column=1, sticky='W')
Radiobutton(root, text="Moderately active", variable=Exercise_factor, value=1.55).grid(row=5, column=2, sticky='W')
Radiobutton(root, text="Very active", variable=Exercise_factor, value=1.725).grid(row=6, column=0, sticky='W')
Radiobutton(root, text="Extra active", variable=Exercise_factor, value=1.9).grid(row=6, column=1, sticky='W')

submit_Button = Button(root, text="Calculate BMI and BMR")
submit_Button.bind("<Button-1>", get_sum)
submit_Button.grid(row=7, column=1)

Label(root, text="Your BMI is: ").grid(row=8, column=0, sticky='W')
BMI_sumEntry = Entry(root)
BMI_sumEntry.grid(row=8, column=1)

Label(root, text="Your BMR is: ").grid(row=9, column=0, sticky='W')
BMR_sumEntry = Entry(root)
BMR_sumEntry.grid(row=9, column=1)

Label(root, text="Your TDEE is: ").grid(row=10, column=0, sticky='W')
TDEE_sumEntry = Entry(root)
TDEE_sumEntry.grid(row=10, column=1)

root.mainloop()