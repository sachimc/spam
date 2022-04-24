import pyautogui
import time

spam_codes_file = open('spam_codes.txt', 'r')
time.sleep(5)

for word in spam_codes_file:
    pyautogui.typewrite(word)
    pyuatohui.press('enter')
