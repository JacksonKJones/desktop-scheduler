# App Entry Point
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Scheduler Desktop")
    label = tk.Label(root, text="Schedule...")
    label.pack(padx=200,pady=200)
    root.mainloop()

if __name__ == "__main__":
    main()