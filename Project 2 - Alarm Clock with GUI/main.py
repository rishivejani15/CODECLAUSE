import datetime
import tkinter as tk
from playsound import playsound
import time

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            status_label.config(text="Wake up!", fg="red")
            stop_button = tk.Button(frame, text="Stop Alarm", command=stop_alarm, bg="red", fg="white", relief=tk.RAISED)
            stop_button.pack(pady=10)
            playsound('alarm_sound.mp3')
            break
        else:
            clock_label.config(text=current_time, fg="black")
            status_label.config(text=f"Waiting for {alarm_time}", fg="black")
            root.update()
            time.sleep(1)

def stop_alarm():
    status_label.config(text="Alarm stopped.", fg="green")
    playsound(None)

root = tk.Tk()
root.title("Alarm Clock")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

clock_label = tk.Label(frame, text="", font=("Arial", 40))
clock_label.pack()

label = tk.Label(frame, text="Enter alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(frame, font=("Arial", 14))
entry.pack()

start_button = tk.Button(frame, text="Set Alarm", command=set_alarm, bg="green", fg="white", relief=tk.RAISED)
start_button.pack(pady=10)

status_label = tk.Label(frame, text="", fg="black", font=("Arial", 14))
status_label.pack()

root.mainloop()
