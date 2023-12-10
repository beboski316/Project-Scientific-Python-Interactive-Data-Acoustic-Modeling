from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np



class AudioModel:
    @staticmethod
    def perform_rt60_analysis(file_path):
        try:
            sample_rate, data = wavfile.read(file_path)
            spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate,
                                                  NFFT=1024, cmap=plt.get_cmap('autumn_r'))

            plt.figure(figsize=(10, 4))
            plt.plot(data, linewidth=1, alpha=0.7, color='#004bc6')
            plt.xlabel('Frequency')
            plt.ylabel('Amplitude')
            plt.title('Waveform')
            plt.grid(True)
            plt.show()

            return sample_rate
        except Exception as e:
            raise e
