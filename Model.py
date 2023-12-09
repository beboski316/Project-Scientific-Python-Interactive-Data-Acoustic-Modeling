from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np

class AudioModel:
    def __init__(self):
        self.data = None
        self.sample_rate = None
        self.file_path = None

    def load_audio(self, file_path):
        self.file_path = file_path
        self.sample_rate, self.data = wavfile.read(file_path)
        self.data = self.data / np.max(np.abs(self.data))

    def calculate_rt60_and_get_plot_data(self):
        freqs, spectrum = self.perform_fft(self.data, self.sample_rate)
        rt60_value, t, data_in_db, points_to_highlight = self.rt60_calculation_with_plot_data(freqs, spectrum)
        return rt60_value, t, data_in_db, points_to_highlight

    def perform_fft(data, sample_rate):
        n = len(data)
        frequency = np.fft.rfftfreq(n, d=1 / sample_rate)
        magnitude = np.abs(np.fft.rfft(data))
        return frequency, magnitude

    def find_target_frequency(freqs, target=1000):
        index = (np.abs(freqs - target)).argmin()
        return freqs[index], index

    def calculate_rt60(data, sample_rate, target_frequency=1000):
        freqs, spectrum = data.perform_fft(data, sample_rate)

        # Find the target frequency
        target_freq, index = data.find_target_frequency(freqs, target_frequency)
        data_for_frequency = spectrum[index]

        # Convert to decibels
        data_in_db = 10 * np.log10(data_for_frequency)

        # Create time array for plotting
        num_samples = len(data)
        t = np.linspace(0, num_samples / sample_rate, num_samples)

        rt60 = 1.0

        return rt60, t, data_in_db

    # Calculate RT60 for the uploaded audio data
    rt60, t, data_in_db = calculate_rt60(data, sample_rate)

    # Plotting the results
    plt.figure(figsize=(12, 6))
    plt.plot(t, data_in_db, label="Decay Curve")
    plt.title(f"RT60 Decay Curve at {int(rt60)}Hz")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Level (dB)")
    plt.legend()
    plt.grid(True)
    plt.show()
