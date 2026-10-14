import tkinter as tk
from tkinter import ttk
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def start_typing():
    time.sleep(2)
    i = 1
    try:
        delays = float(delay_times_entry.get())
    except ValueError:
        print("Please enter a valid number for 'delay'.")
        return

    TheText = text_entry.get("1.0", tk.END).strip()

    try:
        TimesAround = int(end_times_entry.get())
    except ValueError:
        print("Please enter a valid number for 'times'.")
        return

    for _ in range(TimesAround):
        keyboard.type(TheText)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(i,"out of",TimesAround)
        i += 1
        time.sleep(delays)  # Optional delay between iterations


#===============
window = tk.Tk()
window.title("Auto Typer")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#------------1
text_label = ttk.Label(frame, text="Enter your text:")
text_label.grid(row=0, column=0, sticky=tk.W, pady=5)

text_entry = tk.Text(frame, height=10, width=40)
text_entry.grid(row=1, column=0, columnspan=5, pady=5)
#------------2
end_times_label = ttk.Label(frame, text="How many times:")
end_times_label.grid(row=2, column=0, sticky=tk.W, pady=5)

end_times_entry = ttk.Entry(frame)
end_times_entry.grid(row=2, column=1, pady=5)
#------------3
delay_times_label = ttk.Label(frame, text="delay:")
delay_times_label.grid(row=3, column=0, sticky=tk.W, pady=5)

delay_times_entry = ttk.Entry(frame)
delay_times_entry.grid(row=3, column=1, pady=5)
#------------4
start_button = ttk.Button(frame, text="Start", command=start_typing)
start_button.grid(row=4, column=0, columnspan=2, padx=19, pady=10)
#end
window.mainloop()

# https://www.youtube.com/watch?v=vusUfPBsggw&list=PLs3IFJPw3G9LQfo8GYbnPRaD8DKHj9aOJ
# https://www.youtube.com/watch?v=yYALsys-P_w
# https://www.pythontutorial.net/tkinter/tkinter-grid/
