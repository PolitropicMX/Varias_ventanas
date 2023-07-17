from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
##root.title('Codemy.com Learn to code')
##root.geometry("400x200")
style = ttk.Style(root)
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.hist(house_prices,50)
    plt.show()

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.Labelframe(frame, text="Insert Row")
widgets_frame.grid(row=0,column=0, padx=20,pady=20)
my_button = ttk.Button(widgets_frame, text="Show Graph", command=graph)
my_button.grid(row=0,column=0, padx=20,pady=20,sticky="ew")

root.mainloop()
