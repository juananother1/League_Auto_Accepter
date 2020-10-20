from PIL import ImageGrab
import time
import pyautogui

looper = True

x = 972
y = 676

while looper == True:
    image = ImageGrab.grab()
    color = image.getpixel((x, y))
    print(color)
    
    if color == (42, 33, 37):
        pyautogui.moveTo(972, 676)
        time.sleep(1)
        pyautogui.click(972, 676)
        print("DONE")
        looper = False