import tkinter as tk

def round_rect(c, x1, y1, x2, y2, r, **kw):
    points = [
        x1+r,y1, x2-r,y1, x2,y1, x2,y1+r,
        x2,y2-r, x2,y2, x2-r,y2, x1+r,y2,
        x1,y2, x1,y2-r, x1,y1+r, x1,y1
    ]
    return c.create_polygon(points, smooth=True, **kw)

root = tk.Tk()
root.title("Lunexa Chat")
root.state("zoomed")
root.configure(bg="#0b1220")

BG = "#0b1220"
CARD = "#222937"
USER = "#3b82f6"
BOT = "#1a1f25"
INPUT = "#020617"
TEXT = "#e5e7eb"
MUTED = "#94a3b8"

main = tk.Frame(root, bg=BG)
main.pack(expand=True, fill="both")

card = tk.Frame(main, bg=CARD, width=760, height=700)
card.place(relx=0.5, rely=0.5, anchor="center")
card.pack_propagate(False)

tk.Label(card, text="Maya's Chatboot",
         font=("Segoe UI", 32, "bold"),
         fg=TEXT, bg=CARD).pack(pady=(25,5))

tk.Label(card, text="Calm • Expressive • Aesthetic",
         font=("Segoe UI", 12),
         fg=MUTED, bg=CARD).pack()

chat_canvas = tk.Canvas(card, bg=CARD, highlightthickness=0)
chat_canvas.pack(padx=30, pady=20, fill="both", expand=True)

scroll = tk.Scrollbar(chat_canvas, command=chat_canvas.yview)
scroll.pack(side="right", fill="y")

messages = tk.Frame(chat_canvas, bg=CARD)
chat_canvas.create_window((0,0), window=messages, anchor="nw")
chat_canvas.configure(yscrollcommand=scroll.set)

def update_scroll(e=None):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

messages.bind("<Configure>", update_scroll)

def bubble(text, side):
    row = tk.Frame(messages, bg=CARD)
    row.pack(fill="x", pady=6)

    color = USER if side=="right" else BOT
    anchor = "e" if side=="right" else "w"

    canvas = tk.Canvas(row, bg=CARD, highlightthickness=0)
    canvas.pack(anchor=anchor, padx=14)

    label = tk.Label(canvas, text=text,
                     font=("Segoe UI", 13),
                     fg=TEXT, bg=color,
                     wraplength=420, padx=14, pady=8)

    label.update_idletasks()
    w = label.winfo_reqwidth()+10
    h = label.winfo_reqheight()+6
    canvas.config(width=w, height=h)

    round_rect(canvas, 0, 0, w, h, 20, fill=color)
    canvas.create_window(w//2, h//2, window=label)

    chat_canvas.yview_moveto(1)

def bot_reply(text):
    t = text.lower()
    if any(w in t for w in ["hi","hello","hey"]):
        return "Hey 👋 Nice to see you!"
    if "how are you" in t:
        return "I’m doing great 😊 What about you?"
    if "who are you" in t or "your name" in t:
        return "I’m Maya🌙 Your chat companion."
    if "bye" in t:
        return "Goodbye 👋 Take care!"
    return "That’s interesting ✨ Tell me more."

def send():
    msg = entry.get().strip()
    if not msg:
        return
    entry.delete(0,"end")
    bubble(msg, "right")
    root.after(500, lambda: bubble(bot_reply(msg), "left"))

input_row = tk.Frame(card, bg=CARD)
input_row.pack(padx=25, pady=18, fill="x")

input_canvas = tk.Canvas(input_row, bg=CARD, height=50, highlightthickness=0)
input_canvas.pack(side="left", fill="x", expand=True, padx=(0,12))

round_rect(input_canvas, 0, 0, 540, 50, 20, fill=INPUT)
entry = tk.Entry(input_canvas, font=("Segoe UI",14),
                 bg=INPUT, fg=TEXT, bd=0, insertbackground=TEXT)
input_canvas.create_window(270,25, window=entry, width=500, height=30)

btn_canvas = tk.Canvas(input_row, bg=CARD, width=100, height=50, highlightthickness=0)
btn_canvas.pack(side="right")

round_rect(btn_canvas, 0, 0, 100, 50, 20, fill=USER)
tk.Button(btn_canvas, text="Send",
          font=("Segoe UI",14,"bold"),
          bg=USER, fg="white",
          bd=0, cursor="hand2",
          command=send).place(relx=0.5, rely=0.5, anchor="center")

entry.bind("<Return>", lambda e: send())

root.mainloop()
