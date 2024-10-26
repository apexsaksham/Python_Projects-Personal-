import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


# Create the label widget
label = tk.Label(root, font=('Times ', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

def time():
    string = strftime("%H:%M:%S %p \n %D")  # Changed %P to %p for correct AM/PM format
    label.config(text=string)
    label.after(1000, time)

time()  # Call the time function to update the label
root.mainloop()