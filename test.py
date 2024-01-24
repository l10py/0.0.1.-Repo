import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("sapa dia!")

#frame input
input_frame=ttk.Frame(window)
#penempatan Grid, PAck, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen-komponen
nama_depan_label = ttk.Label(window,text="ucup")
nama_depan_label.pack(padx=10,pady=10,fill="x",expand=True)

window.mainloop()
