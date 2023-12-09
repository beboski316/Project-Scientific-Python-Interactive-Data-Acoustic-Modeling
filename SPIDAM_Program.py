import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Analysis function
def perform_rt60_analysis(file_path):
    try:
        # Load the audio file
        sample_rate, data = wavfile.read(file_path)
        data = data / 2**15  # Assuming 16-bit WAV file

        plt.figure(figsize=(10, 4))
        plt.plot(data, linewidth=1, alpha=0.7, color='#004bc6')
        plt.xlabel('Sample Number')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        plt.grid(True)
        plt.show()

        # After plotting, you can update the GUI with the results
        rt60_label.config(text=f"RT60 value: seconds")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
window = tk.Tk()
window.title("RT60 Analysis Tool")

load_button = tk.Button(window, text="Load Audio File", command=lambda: load_audio_file(perform_rt60_analysis))
load_button.pack()

rt60_label = tk.Label(window, text="RT60: Not calculated")
rt60_label.pack()

# Function to load audio file and handle GUI updates
def load_audio_file(analysis_function):
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.aac")])
    if file_path:
        analysis_function(file_path)

window.mainloop()