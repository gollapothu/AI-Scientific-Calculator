import tkinter as tk
from tkinter import scrolledtext
import math

history = []

# Main Window
root = tk.Tk()
root.title("Professional Scientific Calculator")
root.geometry("500x800")
root.configure(bg="#1e1e1e")

# Display
entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        history.append(f"{expression} = {result}")
        history_box.insert(tk.END, f"{expression} = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        history.append(f"√{value} = {result}")
        history_box.insert(tk.END, f"√{value} = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sine():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        history.append(f"sin({value}) = {result}")
        history_box.insert(tk.END, f"sin({value}) = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def cosine():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        history.append(f"cos({value}) = {result}")
        history_box.insert(tk.END, f"cos({value}) = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def tangent():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        history.append(f"tan({value}) = {result}")
        history_box.insert(tk.END, f"tan({value}) = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def logarithm():
    try:
        value = float(entry.get())
        result = math.log10(value)
        history.append(f"log({value}) = {result}")
        history_box.insert(tk.END, f"log({value}) = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def natural_log():
    try:
        value = float(entry.get())
        result = math.log(value)
        history.append(f"ln({value}) = {result}")
        history_box.insert(tk.END, f"ln({value}) = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def exponential():
    try:
        value = float(entry.get())
        result = math.exp(value)
        history.append(f"e^{value} = {result}")
        history_box.insert(tk.END, f"e^{value} = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def factorial():
    try:
        value = int(entry.get())
        result = math.factorial(value)
        history.append(f"{value}! = {result}")
        history_box.insert(tk.END, f"{value}! = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def arcsine():
    try:
        value = float(entry.get())
        result = math.degrees(math.asin(value))
        history.append(f"arcsin({value}) = {result}°")
        history_box.insert(tk.END, f"arcsin({value}) = {result}°\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def arccosine():
    try:
        value = float(entry.get())
        result = math.degrees(math.acos(value))
        history.append(f"arccos({value}) = {result}°")
        history_box.insert(tk.END, f"arccos({value}) = {result}°\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def arctangent():
    try:
        value = float(entry.get())
        result = math.degrees(math.atan(value))
        history.append(f"arctan({value}) = {result}°")
        history_box.insert(tk.END, f"arctan({value}) = {result}°\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def degrees_to_radians():
    try:
        value = float(entry.get())
        result = math.radians(value)
        history.append(f"{value}° = {result} rad")
        history_box.insert(tk.END, f"{value}° = {result} rad\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def radians_to_degrees():
    try:
        value = float(entry.get())
        result = math.degrees(value)
        history.append(f"{value} rad = {result}°")
        history_box.insert(tk.END, f"{value} rad = {result}°\n")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def save_history():
    with open("history.txt", "w") as file:
        for item in history:
            file.write(item + "\n")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text,row,col) in buttons:
    if text == '=':
        btn = tk.Button(root,text=text,command=calculate,bg="#4CAF50",fg="white",font=("Arial",14))
    else:
        btn = tk.Button(root,text=text,command=lambda t=text: click(t),bg="#333333",fg="white",font=("Arial",14))
    btn.grid(row=row,column=col,sticky="nsew",padx=2,pady=2)

# Scientific Buttons
tk.Button(root,text="C",command=clear,bg="red",fg="white").grid(row=5,column=0,sticky="nsew")
tk.Button(root,text="√",command=square_root).grid(row=5,column=1,sticky="nsew")
tk.Button(root,text="x²",command=lambda: click("**2")).grid(row=5,column=2,sticky="nsew")
tk.Button(root,text="log",command=logarithm).grid(row=5,column=3,sticky="nsew")
tk.Button(root,text="ln",command=natural_log).grid(row=5,column=4,sticky="nsew")


tk.Button(root,text="sin",command=sine).grid(row=6,column=0,sticky="nsew")
tk.Button(root,text="cos",command=cosine).grid(row=6,column=1,sticky="nsew")
tk.Button(root,text="tan",command=tangent).grid(row=6,column=2,sticky="nsew")
tk.Button(root,text="e^x",command=exponential).grid(row=6,column=3,sticky="nsew")
tk.Button(root,text="x!",command=factorial).grid(row=6,column=4,sticky="nsew")
tk.Button(root,text="arcsin",command=arcsine).grid(row=7,column=0,sticky="nsew")
tk.Button(root,text="arccos",command=arccosine).grid(row=7,column=1,sticky="nsew")
tk.Button(root,text="arctan",command=arctangent).grid(row=7,column=2,sticky="nsew")
tk.Button(root,text="°→rad",command=degrees_to_radians).grid(row=7,column=3,sticky="nsew")
tk.Button(root,text="rad→°",command=radians_to_degrees).grid(row=7,column=4,sticky="nsew")
tk.Button(root,text="Save",command=save_history).grid(row=7,column=0,columnspan=5,sticky="nsew")
history_box = scrolledtext.ScrolledText(root,width=40,height=10,bg="#252526",fg="white")
history_box.grid(row=8,column=0,columnspan=5,padx=10,pady=10)
root.bind("<Return>", lambda event: calculate())
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
