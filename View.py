import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AudioView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("RT60 Analysis Tool")
        self.load_button = tk.Button(self, text="Load Audio File", command=self.load_file)
        self.load_button.pack()

        self.rt60_label = tk.Label(self, text="RT60 value: Not calculated")
        self.rt60_label.pack()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.controller.load_audio_file(file_path)

    def set_rt60_label(self, text):
        self.rt60_label.config(text=text)

    def plot_data(self, t, data_in_db, points_to_highlight):
        self.ax.clear()
        self.ax.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
        for point in points_to_highlight:
            self.ax.plot(t[point[0]], data_in_db[point[0]], point[1])

        self.ax.set_xlabel('Time (m)')
        self.ax.set_ylabel('Power (db)')
        self.ax.grid()
        self.canvas.draw()
