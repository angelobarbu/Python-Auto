import pyautogui
import time
import random

while True:
    for line in open("fetch_stats.js", "r"):
        time.sleep(20)
        for word in line.split():
            for letter in word:
                pyautogui.press(letter)
                time.sleep(random.randint(1, 5)/10)
            time.sleep(1)
            pyautogui.leftClick()
            pyautogui.press("space")
        pyautogui.press("enter")