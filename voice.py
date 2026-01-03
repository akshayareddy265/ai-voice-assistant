import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    status.set("Listening...")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            output.set(command)
            respond(command)
    except:
        status.set("Try again")
        speak("Sorry, I did not understand")

def respond(command):
    if "hello" in command:
        reply("Hello, how can I help you?")
    elif "time" in command:
        reply(datetime.datetime.now().strftime("Time is %I:%M %p"))
    elif "date" in command:
        reply(datetime.datetime.now().strftime("Today is %d %B %Y"))
    elif "search" in command:
        q = command.replace("search", "")
        reply("Searching")
        webbrowser.open(f"https://www.google.com/search?q={q}")
    else:
        reply("I am still learning")

def reply(text):
    status.set("Speaking...")
    speak(text)
    status.set("Ready!")

def start():
    threading.Thread(target=listen).start()

root = tk.Tk()
root.title("Voice Assistant")
root.state("zoomed")
root.configure(bg="#0b1020")

recognizer = sr.Recognizer()

bg_color = "#0e0e0f"
card_color = "#010a1f"
border_color = "#fdfefe"
accent = "#fefefe"
text_main = "#080000"
muted = "#94a3b8"

main = tk.Frame(root, bg=bg_color)
main.pack(expand=True, fill="both")

card = tk.Frame(
    main,
    bg=card_color,
    width=720,
    height=480,
    highlightbackground=border_color,
    highlightthickness=2
)
card.place(relx=0.5, rely=0.5, anchor="center")
card.pack_propagate(False)

tk.Label(
    card,
    text="Voice Assistant",
    font=("Segoe UI", 38, "bold"),
    fg=accent,
    bg=card_color
).pack(pady=(45, 6))

tk.Label(
    card,
    text="Welcome to your's calm voice assistant...!",
    font=("Segoe UI", 13),
    fg=muted,
    bg=card_color
).pack()

output = tk.StringVar()
tk.Entry(
    card,
    textvariable=output,
    font=("Consolas", 18),
    bg="#808181",
    fg=text_main,
    bd=0,
    justify="center"
).pack(pady=35, padx=80, fill="x")

status = tk.StringVar(value="Ready!")
tk.Label(
    card,
    textvariable=status,
    font=("Segoe UI", 12),
    fg=muted,
    bg=card_color
).pack(pady=10)

btn = tk.Button(
    card,
    text="Start Listening",
    font=("Segoe UI", 15, "bold"),
    bg=accent,
    fg="#020617",
    activebackground="#bfe5f7",
    activeforeground="#020617",
    bd=0,
    padx=40,
    pady=14,
    cursor="hand2",
    command=start
)
btn.pack(pady=30)

root.mainloop()
