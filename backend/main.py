# App Entry Point
import tkinter as tk
from models import Schedule, Task
from datetime import time

def main():
    root = tk.Tk()
    root.title("Scheduler Desktop")
    label = tk.Label(root, text="Schedule...")
    label.pack(padx=200,pady=400)
    root.mainloop()

if __name__ == "__main__":
    main()