import os
import time


def autoSwipe():
    while (True):
        time.sleep(15)
        os.system('adb shell input swipe 300 800 300 100')


if __name__ == '__main__':
    autoSwipe()
