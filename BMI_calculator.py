import tkinter as tk
from math import pow
import ttkbootstrap as ttk

def convert():
    weight_input = entry_weight_val.get()
    print(weight_input)
    height_input = entry_height_val.get()
    height = pow(height_input,2)
    conversion = weight_input / height
    print(conversion)
    formatted_conversion = "{:.2f}".format(conversion)
    output_string.set(formatted_conversion)

    def switch (conversion):
        if conversion < 18.5 :
            return("Underweight")
        elif conversion >= 18.5 and conversion < 25:
            return("Normal Weight")
        elif conversion >= 25 and conversion < 30:
            return("Overweight")
        else:
            return("Obese")
    
    output_BMI_string.set(switch(conversion))


#window
window = ttk.Window(themename='journal')
window.title('BMI calculator')
window.geometry('500x300')

#title
title_label = ttk.Label(master = window, text = "Let's find your BMI", font = "Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_weight_val = tk.DoubleVar()
entry_weight = ttk.Entry(
    master = input_frame, 
    textvariable = entry_weight_val
    )
entry_height_val = tk.DoubleVar()
entry_height = ttk.Entry(
    master = input_frame, 
    textvariable = entry_height_val
    )

button = ttk.Button(master = input_frame, text = "Calculate BMI", command=convert)
entry_weight.pack(padx= 10)
entry_height.pack()
button.pack(side='bottom',pady=10)
input_frame.pack()

#Output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = "Output", 
    font = "Calibri 24", 
    textvariable = output_string)
output_label.pack(pady = 5)

output_BMI_string = tk.StringVar()
output_BMI_label = ttk.Label(
    master = window, 
    text = "Output", 
    font = "Calibri 24", 
    textvariable = output_BMI_string
    )
output_BMI_label.pack(pady = 5)

# run 
window.mainloop()