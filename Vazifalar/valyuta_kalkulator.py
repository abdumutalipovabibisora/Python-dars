import tkinter as tk
from tkinter import messagebox

# Valyutalar va ularning kurslari
KURSLAR = {
    "USD": {"EUR": 0.931, "UZS": 13102, "RUB": 0.089, "GBP": 0.783},
    "EUR": {"USD": 1.073, "UZS": 14042, "RUB": 0.010, "GBP": 0.841},
    "UZS": {"USD": 0.0000763, "EUR": 0.0000713, "RUB": 0.00685, "GBP": 0.0000596},
    "RUB": {"USD": 0.011, "EUR": 0.010, "UZS": 145.98, "GBP": 0.0057},
    "GBP": {"USD": 1.278, "EUR": 1.188, "UZS": 16733, "RUB": 174.67}
}

VALYUTALAR = list(KURSLAR.keys())

# Kursni olish funksiyasi
def kurs_olish(valyuta_1, valyuta_2):
    try:
        kurs = KURSLAR[valyuta_1].get(valyuta_2)
        if kurs:
            return kurs
        else:
            raise Exception(f"{valyuta_1} dan {valyuta_2} ga kurs mavjud emas.")
    except Exception as e:
        messagebox.showerror("Xatolik", f"Kursni olishda xatolik: {e}")
        return None

# Konvertatsiya qilish funksiyasi
def konvertatsiya():
    try:
        miqdor = float(entry_miqdor.get())
        valyuta_1 = valyuta_1_var.get()
        valyuta_2 = valyuta_2_var.get()

        if not valyuta_1 or not valyuta_2:  
            messagebox.showwarning("Ogohlantirish", "Iltimos, valyutalarni tanlang.")
            return

        kurs = kurs_olish(valyuta_1, valyuta_2)
        if kurs:
            konvert_qilingan = miqdor * kurs
            natija_var.set(f"{miqdor:.2f} {valyuta_1} = {konvert_qilingan:.2f} {valyuta_2}\n1 {valyuta_1} = {kurs:.2f} {valyuta_2}")
    except ValueError:
        messagebox.showerror("Xatolik", "Iltimos, to'g'ri son kiriting.")
    except Exception as e:
        messagebox.showerror("Xatolik", f"Xatolik yuz berdi: {e}")

# Tkinter oynasi
oyna = tk.Tk()
oyna.title("Valyuta Konvertori")
oyna.geometry("700x600")
oyna.resizable(False, False)

# Miqdor kiritish
tk.Label(oyna, text="Miqdor kiriting:", font=("Arial", 15), fg="red").pack(pady=(40, 20))
entry_miqdor = tk.Entry(oyna, font=("Arial", 12))
entry_miqdor.pack(pady=20)

# Qaysi valyutadan
valyuta_1_var = tk.StringVar()
label = tk.Label(oyna, text="Qaysi valyutadan:", font=("Arial", 15), fg="red").place(x=140,  y=180)
tk.OptionMenu(oyna, valyuta_1_var, *VALYUTALAR).place(x=180,  y=230)

# Qaysi valyutaga
valyuta_2_var = tk.StringVar()
tk.Label(oyna, text="Qaysi valyutaga:", font=("Arial", 15), fg="red").place(x=400,  y=180)
tk.OptionMenu(oyna, valyuta_2_var, *VALYUTALAR).place(x=450,  y=230)

# Konvertatsiya tugmasi
tk.Button(oyna, text="Konvertatsiya qilish", command=konvertatsiya, font=("Arial", 15), fg="red").place(x=260, y=320)

# Natija
natija_var = tk.StringVar()
tk.Label(oyna, textvariable=natija_var, font=("Arial", 15), fg="green", justify="center").place(x=210, y=440)


oyna.mainloop()


