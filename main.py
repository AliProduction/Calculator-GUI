# This is a simple Python Calculator.
# GUI Calculator
# by Alican Akis

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, title, geometry):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)

        self.drawAllButtons()

    def drawAllButtons(self):
        # Frame 1
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(side="top", pady=10)

        # Frame 2
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(side="top", pady=5)

        # Frame 3
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(side="top", pady=5)

        # Frame 4
        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(side="top", pady=5)

        tk.Button(self.frame1, text="7", width=3, height=3, command=lambda: self.numberButtonClicked(7)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame1, text="8", width=3, height=3, command=lambda: self.numberButtonClicked(8)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame1, text="9", width=3, height=3, command=lambda: self.numberButtonClicked(9)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame1, text="*", width=3, height=3, command=lambda: self.numberButtonClicked('*')).pack(side="left", padx=10, pady=10)

        tk.Button(self.frame2, text="4", width=3, height=3, command=lambda: self.numberButtonClicked(4)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame2, text="5", width=3, height=3, command=lambda: self.numberButtonClicked(5)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame2, text="6", width=3, height=3, command=lambda: self.numberButtonClicked(6)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame2, text="-", width=3, height=3, command=lambda: self.numberButtonClicked('-')).pack(side="left", padx=10, pady=10)

        tk.Button(self.frame3, text="1", width=3, height=3, command=lambda: self.numberButtonClicked(1)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame3, text="2", width=3, height=3, command=lambda: self.numberButtonClicked(2)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame3, text="3", width=3, height=3, command=lambda: self.numberButtonClicked(3)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame3, text="+", width=3, height=3, command=lambda: self.numberButtonClicked('+')).pack(side="left", padx=10, pady=10)

        tk.Button(self.frame4, text="AC", width=3, height=3, command=lambda: self.clearOperations()).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame4, text="0", width=3, height=3, command=lambda: self.numberButtonClicked(0)).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame4, text=",", width=3, height=3, command=lambda: self.numberButtonClicked(',')).pack(side="left", padx=10, pady=10)
        tk.Button(self.frame4, text="=", width=3, height=3, command=lambda: self.startCalculating()).pack(side="left", padx=10, pady=10)

    def start(self):
        self.root.mainloop()

    def numberButtonClicked(self, item):
        self.entry.insert(tk.END, item)
        print(f"💻🛡️ Button with value: {item} clicked 🌟")

    def clearOperations(self):
        self.entry.delete(0, tk.END)
        print("💻🛡️ Entry successfully cleared")

    def startCalculating(self):
        if self.entry.get() != '' and not any(char.isalpha() for char in self.entry.get()):
            solution = eval(self.entry.get().replace(',', '.'))
            self.clearOperations()
            self.entry.insert(0, solution)
            print(f"💻🛡️ Solution: {solution}")
        else:
            messagebox.showinfo("🛑 Fehler", "Es gibt nichts zu berechnen!")
            self.clearOperations()



if __name__ == '__main__':
    print("💻🛡️ Calculator started 🚀")
    cal = Calculator('💻 Taschenrechner', '300x400')
    cal.start()
