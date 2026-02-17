from tkinter import *
from tkinter import messagebox
from tkinter import Button
import tkinter as tk
from math import *
root=Tk()
root.title("Simple Calculator")
root.iconphoto(False,PhotoImage(file='./calculator.png'))

e=Entry(root,width=30,borderwidth=5,font=('Calibri 15'))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def b_click(num):
    #e.delete(0,END)
    e.insert(tk.END,num)
    

def equ_clicked():
    a=e.get()
    y=eval(a)
    e.delete(0,END)
    e.insert(0,y)

def clr_clicked():
     e.delete(0,END)
    
b1=Button(root,text="1",padx=40,pady=20,command=lambda:b_click(1))
b2=Button(root,text="2",padx=40,pady=20,command=lambda:b_click(2))
b3=Button(root,text="3",padx=40,pady=20,command=lambda:b_click(3))
b4=Button(root,text="4",padx=40,pady=20,command=lambda:b_click(4))
b5=Button(root,text="5",padx=40,pady=20,command=lambda:b_click(5))
b6=Button(root,text="6",padx=40,pady=20,command=lambda:b_click(6))
b7=Button(root,text="7",padx=40,pady=20,command=lambda:b_click(7))
b8=Button(root,text="8",padx=40,pady=20,command=lambda:b_click(8))
b9=Button(root,text="9",padx=40,pady=20,command=lambda:b_click(9))
b0=Button(root,text="0",padx=40,pady=20,command=lambda:b_click(0))
b_add=Button(root,text="+",padx=40,pady=20,command=lambda:b_click("+"))
b_sub=Button(root,text="-",padx=40,pady=20,command=lambda:b_click("-"))
b_mul=Button(root,text="x",padx=40,pady=20,command=lambda:b_click("*"))
b_div=Button(root,text="/",padx=40,pady=20,command=lambda:b_click("/"))
b_equ=Button(root,text="=",padx=40,pady=20,command=lambda:equ_clicked())
b_clr=Button(root,text="Clear",padx=40,pady=20,command=lambda:clr_clicked())
b_B=Button(root,text="(",padx=40,pady=20,command=lambda:b_click("("))
b_B1=Button(root,text=")",padx=40,pady=20,command=lambda:b_click(")"))
b_00=Button(root,text="00",padx=40,pady=20,command=lambda:b_click("00"))
b9.grid(row=1,column=0)
b8.grid(row=1,column=1)
b7.grid(row=1,column=2)
b6.grid(row=2,column=0)
b5.grid(row=2,column=1)
b4.grid(row=2,column=2)
b3.grid(row=3,column=0)
b2.grid(row=3,column=1)
b1.grid(row=3,column=2)
b0.grid(row=4,column=0)
b_add.grid(row=4,column=1)
b_sub.grid(row=4,column=2)
b_mul.grid(row=5,column=0)
b_div.grid(row=5,column=1)
b_equ.grid(row=5,column=2)
b_clr.grid(row=6,column=0)
b_B.grid(row=6,column=1)
b_B1.grid(row=6,column=2)
b_00.grid(row=7,column=0)
root.mainloop

