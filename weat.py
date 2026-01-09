import customtkinter as ctk
import requests
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def get_weather():
    city = city_entry.get().strip()
    if not city:
        return

    try:
        data = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5).json()
        cur = data["current_condition"][0]
        forecast = data["weather"]

        city_label.configure(text=city.title())
        temp_label.configure(text=f"{cur['temp_C']}°C")
        desc_label.configure(text=cur["weatherDesc"][0]["value"])
        meta_label.configure(
            text=f"Humidity {cur['humidity']}%   Wind {cur['windspeedKmph']} km/h"
        )

        draw_graph([int(h["tempC"]) for h in forecast[0]["hourly"][:8]])

        for i, day in enumerate(forecast[:7]):
            day_cards[i].configure(
                text=f"{day['date'][-2:]}\n{day['maxtempC']}° / {day['mintempC']}°"
            )

    except:
        city_label.configure(text="Location not found")

def draw_graph(temps):
    graph.delete("all")
    w, h = 600, 180
    max_t, min_t = max(temps), min(temps)

    points = []
    for i, t in enumerate(temps):
        x = i * (w // (len(temps)-1))
        y = h - int((t-min_t)/(max_t-min_t+1)*140) - 20
        points.append((x,y))

    for i in range(len(points)-1):
        graph.create_line(
            points[i][0], points[i][1],
            points[i+1][0], points[i+1][1],
            fill="#facc15", width=3, smooth=True
        )

app = ctk.CTk()
app.title("Maya Weather Pro")
app.geometry("1000x700")

main = ctk.CTkFrame(app, corner_radius=30)
main.pack(expand=True, fill="both", padx=30, pady=30)

top = ctk.CTkFrame(main, corner_radius=25)
top.pack(fill="x", padx=30, pady=20)

city_label = ctk.CTkLabel(top, text="Enter City", font=("Segoe UI", 22, "bold"))
city_label.pack(anchor="w", padx=20, pady=(15,5))

desc_label = ctk.CTkLabel(top, text="", font=("Segoe UI", 14))
desc_label.pack(anchor="w", padx=20)

temp_label = ctk.CTkLabel(top, text="", font=("Segoe UI", 64, "bold"))
temp_label.pack(anchor="w", padx=20, pady=(5,0))

meta_label = ctk.CTkLabel(top, text="", font=("Segoe UI", 13))
meta_label.pack(anchor="w", padx=20, pady=(0,15))

search = ctk.CTkFrame(main, corner_radius=20)
search.pack(pady=10)

city_entry = ctk.CTkEntry(
    search, width=300, height=40,
    placeholder_text="Enter city"
)
city_entry.pack(side="left", padx=10)

ctk.CTkButton(
    search, text="Get Weather",
    width=150, height=40,
    command=get_weather
).pack(side="left", padx=10)

graph_frame = ctk.CTkFrame(main, corner_radius=25)
graph_frame.pack(fill="x", padx=30, pady=20)

graph = tk.Canvas(
    graph_frame, width=600, height=180,
    bg="#111827", highlightthickness=0
)
graph.pack(pady=15)

days = ctk.CTkFrame(main, corner_radius=25)
days.pack(fill="x", padx=30, pady=20)

day_cards = []
for _ in range(7):
    lbl = ctk.CTkLabel(
        days, text="--\n--° / --°",
        width=100, height=80,
        corner_radius=15,
        font=("Segoe UI", 14)
    )
    lbl.pack(side="left", padx=10)
    day_cards.append(lbl)

app.mainloop()
