#PYTHON PROGRAMMING INTERNSHIP
#PROJECT 2- BMI CALCULATOR
#NAME: SEJAL DAROLIYA

#Importing all the required modules and libraries
import customtkinter
from tkinter import *
from tkinter import messagebox

#Setting up the background dimensions
app = customtkinter.CTk()
app.geometry("300x400")
app.title("BMI CALCULATOR")
app.config(bg='lavender')

font1 = ("Arial",30,"bold")
font2 = ("Arial",18,"bold")
font3 = ("Arial",25,"bold")

#Adding the entry boxes and labels
title_label = customtkinter.CTkLabel(app, font = font1, text = "BMI CALCULATOR", text_color="#000", bg_color="#FFFFFF")
title_label.place(x=20, y=20)

weight_label = customtkinter.CTkLabel(app, font = font3, text = "WEIGHT", text_color="#000", bg_color="#FFB6C1")
weight_label.place(x=20, y=80)

height_label = customtkinter.CTkLabel(app, font = font3, text = "HEIGHT", text_color="#000", bg_color="#E6E6FA")
height_label.place(x=20, y=150)

weight_entry = customtkinter.CTkEntry(app, font = font2, text_color="#000", fg_color="#FFF5EE", border_color="#fff")
weight_entry.place(x=20, y=110)

height_entry = customtkinter.CTkEntry(app, font = font2, text_color="#000", fg_color="#F0F8FF", border_color="#fff")
height_entry.place(x=20, y=180)

#Setting the options for the required fields
weight_options = ['Kg','ibs']
height_options = ['cm', 'ft']
variable1 = StringVar()
variable2 = StringVar()

weight_options = customtkinter.CTkComboBox(app, font = font2, text_color="#000", fg_color="#FFF5EE", dropdown_hover_color="#06911f", values=weight_options, variable=variable1,width=80)
weight_options.place(x=180,y=110)
weight_options.set('Kg')

height_options = customtkinter.CTkComboBox(app, font = font2, text_color="#000", fg_color="#F0F8FF", dropdown_hover_color="#06911f", values=height_options, variable=variable2,width=80)
height_options.place(x=180,y=180)
height_options.set('cm')
txt=StringVar()

#Function calculate_bmi() - calculates the BMI from the inputed data
def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        if variable2.get() == "ft":
            height *= 30.48
        if variable1.get() == "ibs":
            weight *= 0.453592
        bmi = weight / ((height/100)**2)
        result_label.configure(text="Your BMI is : {:.1f}".format(bmi))
        if(bmi <= 18.5) :
            txt.set("Underweight")
        elif(bmi <= 24.5):
            txt.set("Normal")
        elif (bmi <= 29.9):
            txt.set("Overweight")
        elif (bmi <= 34.4):
            txt.set("Obese I")
        elif (bmi <= 39.9):
            txt.set("Obese II")
        else:
            txt.set("Obese III")
    except ValueError:
        messagebox.showerror("Error","Enter a valid Number!")
    except ZeroDivisionError:
        messagebox.showerror("Error","Height cannot be zero!")

#Buttons
calculate_button = customtkinter.CTkButton(app, command = calculate_bmi, font = font2, text_color="#fff", text="Calculate BMI", fg_color="#06911f", bg_color="#000", cursor = "hand2", corner_radius=5, width=200)
calculate_button.place(x=50, y=230)

result_label = customtkinter.CTkLabel(app, text= " ", font = font3, text_color="#fff", bg_color="#000")
result_label.place(x=30,y=280)

result_label2 = customtkinter.CTkLabel(app, textvariable=txt, font = font3, text_color="#fff", bg_color="#000")
result_label2.place(x=30,y=350)

#RUNS THE PROGRAM
app.mainloop()


