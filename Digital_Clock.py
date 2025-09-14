import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Arial', 48), fg='blue')
label.pack(pady=20)

update_clock()
root.mainloop()
