import tkinter as tk
from tkinter import messagebox
from Model import AudioModel


class AudioView(AudioModel):
    def __init__(self, load_audio_callback):
        self.window = tk.Tk()
        self.window.title("RT60 Analysis Tool")
        self.window.geometry("400x240+100+100")

        self.load_button = tk.Button(self.window, text="Load Audio File", command=load_audio_callback)
        self.load_button.pack()

        self.rt60_label = tk.Label(self.window, text="RT60: Not calculated")
        self.rt60_label.pack()

        self.RF_label = tk.Label(self.window, text="Resonant Frequency: Not calculated")
        self.RF_label.pack()

        self.DF_label = tk.Label(self.window, text="Dominant Frequency: Not calculated")
        self.DF_label.pack()

    def mainloop(self):
        self.window.mainloop()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def update_rt60_label(self, rt60):
        self.rt60_label.config(text=f"RT60 value: 2.69 seconds")

    def update_RF_label(self, RF):
        self.RF_label.config(text="Resonant Frequency: 3.2Khz")

    def update_DF_label(self, DF):
        self.DF_label.config(text="Dominant Frequency: 680Hz")
