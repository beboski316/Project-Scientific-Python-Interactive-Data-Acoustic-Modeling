import tkinter as tk
from tkinter import messagebox

class AudioView:
    def __init__(self, load_audio_callback):
        self.window = tk.Tk()
        self.window.title("RT60 Analysis Tool")

        self.load_button = tk.Button(self.window, text="Load Audio File", command=load_audio_callback)
        self.load_button.pack()

        self.rt60_label = tk.Label(self.window, text="RT60: Not calculated")
        self.rt60_label.pack()

    def mainloop(self):
        self.window.mainloop()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def update_rt60_label(self, rt60_value):
        self.rt60_label.config(text=f"RT60 value: {rt60_value} seconds")
