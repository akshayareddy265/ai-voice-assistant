import tkinter as tk
from tkinter import ttk
import random
import string

words = [
    "Nova","Cloud","Zen","Pixel","Shift",
    "Node","Core","Orbit","Prime","Echo"
]

used = set()

def generate():
    length = int(slider.get())
    base = random.choice(words) + random.choice(words)
    sym = random.choice("_@#")
    num = random.randint(10, 99)
    end = random.choice(string.ascii_uppercase)
    pwd = f"{base}{sym}{num}{end}"

    while pwd in used or len(pwd) < length:
        pwd += random.choice(string.ascii_letters)

    pwd = pwd[:length]
    used.add(pwd)
    result.set(pwd)

def copy():
    root.clipboard_clear()
    root.clipboard_append(result.get())

root = tk.Tk()
root.title("Automatic Password Generator")
root.state("zoomed")
root.configure(bg="#0b1f3a")

accent = "#e5ecf6"
text_dark = "#0f172a"
text_light = "#334155"

style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=("Segoe UI", 12), padding=10)
style.configure("TScale", background="#0b1f3a")

main = tk.Frame(root, bg="#0b1f3a")
main.pack(expand=True, fill="both")

card = tk.Frame(main, bg=accent, width=700, height=460)
card.place(relx=0.5, rely=0.5, anchor="center")
card.pack_propagate(False)

title = tk.Label(
    card,
    text="Automatic Password Generator",
       font=("Segoe UI", 34, "bold"),
    fg=text_dark,
    bg=accent
)
title.pack(pady=(45, 8))

tag = tk.Label(
    card,
    text="clean • professional • secure",
    font=("Segoe UI", 12),
    fg=text_light,
    bg=accent
)
tag.pack()

result = tk.StringVar()
entry = tk.Entry(
    card,
    textvariable=result,
    font=("Consolas", 22),
    bg=accent,
    fg=text_dark,
    bd=0,
    justify="center"
)
entry.pack(pady=35, padx=70, fill="x")

tk.Label(
    card,
    text="Password Length",
    font=("Segoe UI", 12),
    fg=text_light,
    bg=accent
).pack()

slider = ttk.Scale(card, from_=12, to=24, orient="horizontal")
slider.set(16)
slider.pack(pady=10, padx=140, fill="x")

btns = tk.Frame(card, bg=accent)
btns.pack(pady=35)

ttk.Button(btns, text="Generate", command=generate).grid(row=0, column=0, padx=20)
ttk.Button(btns, text="Copy", command=copy).grid(row=0, column=1, padx=20)

generate()
root.mainloop()
