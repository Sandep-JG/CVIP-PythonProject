import tkinter as tk
import time
import threading
import random

class TypingSpeed:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600")
        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample = tk.Label(self.frame, text=random.choice(self.texts), font=("Arial", 18))
        self.sample.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input = tk.Entry(self.frame, width=30, font=("Arial", 24))
        self.input.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input.bind("<KeyRelease>", self.start)
        self.speed = tk.Label(self.frame, text="Words Per Second: 0.00 WPS\nWords Per Minute: 0.00 WPM", font=("Arial", 18))
        self.speed.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        self.reset = tk.Button(self.frame, text="Reset", command=self.reset, font=("Arial", 24))
        self.reset.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False
        self.correctly_typed = False

        self.sample.config(text=random.choice(self.texts))

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if event.keycode not in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample.cget('text').startswith(self.input.get()):
            self.input.config(fg="red")
        else:
            self.input.config(fg="black")
        if self.input.get() == self.sample.cget('text'):
            self.running = False
            self.correctly_typed = True
            self.input.config(fg="green")

    def time_thread(self):
        self.started = True
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            if not self.correctly_typed:
                wps = len(self.input.get().split(" ")) / self.counter
                wpm = wps * 60
                self.speed.config(text=f"Words Per Second: {wps:.2f} WPS\nWords Per Minute: {wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed.config(text="Words Per Second: 0.00 WPS\nWords Per Minute: 0.00 WPM")
        self.sample.config(text=random.choice(self.texts))
        self.input.delete(0, tk.END)

TypingSpeed()
