from tkinter import filedialog
from Model import AudioModel
from View import AudioView

class AudioController:
    def __init__(self):
        self.model = AudioModel()
        self.view = AudioView(self.load_audio_file)

    def run(self):
        self.view.mainloop()

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.aac")])
        if file_path:
            try:
                rt60 = self.model.perform_rt60_analysis(file_path)
                self.view.update_rt60_label(rt60)
                self.view.update_RF_label(RF=3.2)
                self.view.update_DF_label(DF=680)
            except Exception as e:
                self.view.show_error(f"An error occurred: {e}")

if __name__ == "__main__":
    controller = AudioController()
    controller.run()
