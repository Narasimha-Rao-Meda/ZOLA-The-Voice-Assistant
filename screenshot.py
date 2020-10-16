import pyautogui
import os

def take_screenshot():
    path = os.getcwd()
    screenshot_jpg = pyautogui.screenshot()
    print(path)
    path = path.replace('\\','\\\\')
    screenshot_jpg.save(path+'\\Images\\screenshot.jpg')