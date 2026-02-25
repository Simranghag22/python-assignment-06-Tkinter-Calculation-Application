# ----------------------------------------------------------
# Project: Simple Calculator using Tkinter
# Description: A basic calculator that performs
# addition, subtraction, multiplication and division.
# ----------------------------------------------------------
#step 1: Importing the required module
from tkinter import *

#Step 2: GUI Interaction
window = Tk()                              #Create main window
window.geometry ("500x500")                #Set window size
window.title("Calculator")                 #Set window title

#Step 3: Adding Inputs
#Creating Entry Widget (Display Screen) => Displays numbers and results
e=Entry(window, width=50, border=5)
e.place(x=0,y=0)

#Buttons
"""
This function is called whenever a number button is pressed. It retrieves the current value from the entry box,
appends the clicked number and updates the display."""

def click(num):
    result = e.get()                   #Get current text from entry
    e.delete(0, END)                   # Clear entry box
    e.insert(0,str(result)+str(num))   #Append new number

#Creating the Number Buttons (0-9)

b=Button(window, text='1', width=12, command = lambda:click(1))
b.place(x=10,y=60)

b=Button(window, text='2', width=12,command = lambda:click(2))
b.place(x=80,y=60)

b=Button(window, text='3', width=12,command = lambda:click(3))
b.place(x=170,y=60)

b=Button(window, text='4', width=12,command = lambda:click(4))
b.place(x=10,y=120)

b=Button(window, text='5', width=12,command = lambda:click(5))
b.place(x=80,y=120)

b=Button(window, text='6', width=12,command = lambda:click(6))
b.place(x=170,y=120)

b=Button(window, text='7', width=12,command = lambda:click(7))
b.place(x=10,y=180)

b=Button(window, text='8', width=12,command = lambda:click(8))
b.place(x=80,y=180)

b=Button(window, text='9', width=12,command = lambda:click(9))
b.place(x=170,y=180)

b=Button(window, text='0', width=12,command = lambda:click(0))
b.place(x=10,y=240)

#Adding Operators

def add():
    n1 = e.get()        #stores the first number and sets operation to addition
    global math
    math="addition"
    global i
    i = int(n1)
    e.delete(0, END)  #the values present in the entry box should be deleted and stored

b=Button(window, text='+', width=12,command = add)
b.place(x=80,y=240)

def sub():
    n1 = e.get()      #stores the first number and sets operation to subtraction.
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b=Button(window, text='-', width=12,command = sub)
b.place(x=170,y=240)

def mult():
    n1 = e.get()      #stores the first number and sets operation to multiplication
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)
b=Button(window, text='*', width=12,command = mult)
b.place(x=10,y=300)

def div():
    n1 = e.get()    #stores the first number and sets operation to division.
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)
b=Button(window, text='/', width=12,command = div)
b.place(x=80,y=300)

#Creating equal button function
"""Performs calculation based on selected operation
   and displays the result."""

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

b=Button(window, text='=', width=12, command = equal)
b.place(x=170,y=300)

#Creating clear button function
"""Clears the entry display."""
def clear():
    e.delete(0, END)

b=Button(window, text='clear', width=12, command = clear)
b.place(x=10,y=350)


#Step 4: mainloop to run the application
mainloop()     #keeps the window running