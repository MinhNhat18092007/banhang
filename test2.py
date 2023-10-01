import cv2
from adbutils import adb
from PIL import Image
from pyzbar.pyzbar import decode
import subprocess
import pyperclip
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import colorama
from colorama import Fore, init
import inquirer
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from collections import defaultdict
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput import keyboard
import time
from threading import Timer
from threading import Thread
import numpy as np
import keyboard as KB

def capture_screenshot_to_file(device, filename):
    device.shell("screencap -p /sdcard/screenshot.png")
    
    # Trích xuất hình ảnh từ thiết bị
    device.sync.pull("/sdcard/screenshot.png", filename)
    
    # Xóa hình ảnh từ thiết bị sau khi trích xuất
    device.shell("rm /sdcard/screenshot.png")



def getDevice(i):
    devices = list(adb.device_list())
    
    if i < len(devices):
        return devices[i]
    else:
        return None

deviceId = getDevice(0)
def click_ocr(image,device):
    screenshot_filename = "image/screen.png"
    capture_screenshot_to_file(device, screenshot_filename)

    img = cv2.imread(image)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("image/screen.png", 0)

    w, h = template.shape[1], template.shape[0]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    THRESHOLD = 0.9
    loc = np.where(res >= THRESHOLD)
    # Draw boudning box
    for y, x in zip(loc[0], loc[1]):

        return device.click(x+6,y+6)
        break
        
    
goi = f"adb -s {deviceId.serial} shell am start -a android.intent.action.DIAL -d tel:0867809383"
# goi = f"adb -s {deviceId.serial} shell am start -a android.intent.action.DIAL -d tel:0397498285"
print(goi)
subprocess.run(goi, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# time.sleep(2)
click_ocr("image/test.png", deviceId)

checkendcall = True
while checkendcall:
    if KB.is_pressed('f2'):
        click_ocr("image/end1sim.png", deviceId)
        checkendcall = False



