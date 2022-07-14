from tkinter import Tk, Button, Label
from tkinter import ttk
from tkinter import Frame
from threading import Thread

from speech_to_text_model import main
import vlc

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Speech to Text Transcription Module")
        self.geometry("400x150")
        self.resizable(False, False)
        self.style = ttk.Style(self)

        self.title_label = ttk.Label(self, text="ASL Speech to Text", font=("Arial", 20)).place(x=70, y=10)

        self.s_button_style = ttk.Style()
        self.s_button_style.configure('B1.TButton', background='#15CB05', activecolor='#15CB05')
        self.start_button = ttk.Button(self, text="Start", style="B1.TButton", command=self.start)
        self.start_button.place(x=70, y=60, width=100, height=50)

        self.p_button_style = ttk.Style()
        self.p_button_style.configure('B2.TButton', background='#DFA309')
        self.pause_button = ttk.Button(self, style="B2.TButton", text="Stop", command=self.pause)
        self.pause_button.place(x=230, y=60, width=100, height=50)

    def start(self):

        self.frame = Frame(self, width=50, height=20)
        self.frame.pack()
        display = Frame(self.frame, bd=5)
        display.place(relwidth=1, relheight=1)

        # config.detection_mode = 1
        print("START")
        # Thread(target=main).start()
        main(self, display)

    def pause(self):
        # config.detection_mode = 0
        print("PAUSE")


if __name__ == '__main__':
    app = App()
    app.mainloop()
