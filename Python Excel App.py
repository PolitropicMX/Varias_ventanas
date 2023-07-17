import tkinter as tk
from tkinter import ttk
import pandas as pd
import openpyxl

def load_data():
    path = r'C:\Users\Fer\AppData\Local\Programs\Python\Python310\los_codigos\tkinter\Forest-ttk-theme-master\antoine.xlsx'
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
##    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name,text=col_name)
    for value_tuple in list_values[1:]:
        treeview.insert('',tk.END, values=value_tuple)

def insert_row():
    name = status_combobox.get()
    A = float(spinbox.get())
    subscription = status_combobox.get()
    status = "vacio" if a.get() else "LLeno"
    print(name,A,subscription,status)
    # Insert row into Excel sheet

    # Insert row into treeview

def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

# Hierarchy

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")
compounds = []
df = pd.read_csv('antoine.csv')
for i,compound in enumerate(df["Compound Name"]):
    compounds.append(str(compound))
headers = df.head()

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.Labelframe(frame, text="Insert Row")
widgets_frame.grid(row=0,column=0, padx=20,pady=20)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0,"Compound")
name_entry.bind("<FocusIn>",lambda e: name_entry.delete('0','end'))
name_entry.grid(row=0,column=0,padx=5,pady=[0, 5],sticky="ew")

spinbox = ttk.Spinbox(widgets_frame,from_=18, to=100)
spinbox.insert(0,"Molar Mass")
spinbox.grid(row=1,column=0,padx=5,pady=[0, 5],sticky="ew")

status_combobox = ttk.Combobox(widgets_frame, values = compounds)
status_combobox.current(0)
status_combobox.grid(row=2, column = 0,padx=5,pady=[0, 5], sticky="ew")

a = tk.BooleanVar()
checkbutton = ttk.Checkbutton(widgets_frame, text="Employed", variable=a)
checkbutton.grid(row=3,column=0,sticky="nsew")

button = ttk.Button(widgets_frame, text="Insert", command=insert_row)
button.grid(row=4,column=0,sticky="nsew")

separator = ttk.Separator(widgets_frame)
separator.grid(row=5,column=0,padx=(20,10),pady=10,sticky="ew")

mode_switch = ttk.Checkbutton(widgets_frame, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=6,column=0,padx=5,pady=10,sticky="nsew")

treeframe = ttk.Frame(frame)
treeframe.grid(row=0,column=1,pady=10)
treescroll = ttk.Scrollbar(treeframe)
treescroll.pack(side="right", fill="y")


cols = ("Compound Name","A","B","C")
treeview = ttk.Treeview(treeframe,show="headings",
                        yscrollcommand=treescroll.set,
                        columns=cols,height=13)
treeview.column("Compound Name",width=100)
treeview.column("A",width=50)
treeview.column("B",width=50)
treeview.column("C",width=50)
treeview.pack()
treescroll.config(command=treeview.yview)
load_data()
#Last line of code
root.mainloop
