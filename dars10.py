import tkinter as tk

oyna = tk.Tk()
oyna.title("Label")
oyna.geometry("600x500")

label = tk.Label(oyna, text="Salom, dunyo!",bg="pink", width=20, height=3)
label.pack(pady=100)     

def matnni_ozgartir():
    label.config(text="Assalomu alaykum")

tugma = tk.Button(oyna, text="Matnni o‘zgartirish",bg="green",width=20, height=3, command=matnni_ozgartir)
tugma.pack()

oyna.mainloop()       
