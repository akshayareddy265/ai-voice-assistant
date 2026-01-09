import tkinter as tk

def round_rect(c, x1, y1, x2, y2, r, **kw):
    points = [
        x1+r,y1, x2-r,y1, x2,y1, x2,y1+r,
        x2,y2-r, x2,y2, x2-r,y2, x1+r,y2,
        x1,y2, x1,y2-r, x1,y1+r, x1,y1
    ]
    return c.create_polygon(points, smooth=True, **kw)

def calculate():
    try:
        w = float(weight_entry.get())
        h = float(height_entry.get()) / 100
        bmi = w / (h*h)
        bmi_var.set(f"{bmi:.1f}")

        if bmi < 18.5:
            status_var.set("Underweight")
            bmi_label.config(fg="#78350f")
        elif bmi < 25:
            status_var.set("Normal")
            bmi_label.config(fg="#166534")
        elif bmi < 30:
            status_var.set("Overweight")
            bmi_label.config(fg="#9a3412")
        else:
            status_var.set("Obese")
            bmi_label.config(fg="#7f1d1d")
    except:
        bmi_var.set("--")
        status_var.set("Enter height and weight")

root = tk.Tk()
root.title("BMI Calculator")
root.state("zoomed")
root.configure(bg="#3f2a1d")

canvas = tk.Canvas(root, bg="#3f2a1d", highlightthickness=0)
canvas.pack(fill="both", expand=True)

card_color = "#e7d3b1"
card_w, card_h = 560, 760
x1 = (root.winfo_screenwidth()-card_w)//2
y1 = (root.winfo_screenheight()-card_h)//2
x2, y2 = x1+card_w, y1+card_h

round_rect(canvas, x1, y1, x2, y2, 40, fill=card_color, outline="#fef3c7", width=2)

card = tk.Frame(canvas, bg=card_color)
canvas.create_window((x1+x2)//2, (y1+y2)//2,
                     window=card, width=card_w-30, height=card_h-30)

tk.Label(card, text="BMI Calculator",
         font=("Segoe UI",36,"bold"),
         fg="#3f2a1d", bg=card_color).pack(pady=(35,5))

tk.Label(card, text="Body mass index calculator",
         font=("Segoe UI",13),
         fg="#7c5c3e", bg=card_color).pack()

def rounded_entry(parent):
    c = tk.Canvas(parent, width=300, height=45,
                  bg=card_color, highlightthickness=0)
    round_rect(c, 0, 0, 300, 45, 22,
               fill="#fffaf0", outline="#d6c1a0")
    e = tk.Entry(c, font=("Segoe UI",16),
                 bg="#fffaf0", fg="#3f2a1d",
                 bd=0, justify="center")
    c.create_window(150, 23, window=e, width=260, height=28)
    return c, e

tk.Label(card, text="Weight (kg)",
         font=("Segoe UI",14),
         fg="#3f2a1d", bg=card_color).pack(pady=(35,6))
w_box, weight_entry = rounded_entry(card)
w_box.pack()

tk.Label(card, text="Height (cm)",
         font=("Segoe UI",14),
         fg="#3f2a1d", bg=card_color).pack(pady=(25,6))
h_box, height_entry = rounded_entry(card)
h_box.pack()

btn = tk.Canvas(card, width=300, height=60,
                bg=card_color, highlightthickness=0)
btn.pack(pady=35)
round_rect(btn, 0, 0, 300, 60, 30,
           fill="#d6c1a0", outline="#c9b08b")

tk.Button(btn, text="Calculate BMI",
          font=("Segoe UI",16,"bold"),
          bg="#d6c1a0", fg="#3f2a1d",
          bd=0, cursor="hand2",
          command=calculate).place(relx=0.5, rely=0.5, anchor="center")

result_box = tk.Canvas(card, width=300, height=90,
                       bg=card_color, highlightthickness=0)
result_box.pack()
round_rect(result_box, 0, 0, 300, 90, 30,
           fill="#fffaf0", outline="#c9b08b")

result_frame = tk.Frame(result_box, bg="#fffaf0")
result_box.create_window(150, 45, window=result_frame)

bmi_var = tk.StringVar(value="")
bmi_label = tk.Label(result_frame, textvariable=bmi_var,
                     font=("Segoe UI",38,"bold"),
                     bg="#fffaf0", fg="#78350f")
bmi_label.pack()

status_var = tk.StringVar(value="Enter height and weight")
tk.Label(card, textvariable=status_var,
         font=("Segoe UI",20),
         fg="#311e0c", bg=card_color).pack(pady=(10,0))

root.mainloop()
