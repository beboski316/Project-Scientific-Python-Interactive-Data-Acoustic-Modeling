from tkinter import messagebox
from Model import AudioModel
from View import AudioView

class AudioController:
    def __init__(self):
        self.model = AudioModel()
        self.view = AudioView(self)

    def load_audio_file(self, file_path):
        try:
            self.model.load_audio(file_path)
            rt60_value, t, data_in_db, points_to_highlight = self.model.calculate_rt60_and_get_plot_data()
            self.view.set_rt60_label(f"RT60 Value: {rt60_value}")
            self.view.plot_data(t, data_in_db, points_to_highlight)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    controller = AudioController()
    controller.run()
