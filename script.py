import pyautogui
import time

while True:
    time.sleep(15)
    for line in open("fetch_stats.py", "r"):
        for word in line.split():
            time.sleep(1.2)
            pyautogui.typewrite(word)
        pyautogui.press("enter")