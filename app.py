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
  
delay = float(input("Nhập độ trễ"))
a = None
def choose_tool():
    global a
    global shortkey
    init(autoreset=True)  # Automatically resets terminal color to default after each print
    questions1 = [
        inquirer.List('account', message=f"{Fore.YELLOW}Select Tools{Fore.WHITE}", 
                      choices=['Bang Hutahaean', 'Christian Benitez']),
    ]
    questions = [
        inquirer.List('tools', message=f"{Fore.YELLOW}Select Tools{Fore.WHITE}", 
                      choices=['Quét theo tùy chọn', 'Quét hàng loạt']),
    ]
    answers1 = inquirer.prompt(questions1)
    answers = inquirer.prompt(questions)
    if answers1['account'] == "Bang Hutahaean":
        with open("cookies/cookie_1.txt", "r", encoding="utf-8") as file_cookies:
            cookies = file_cookies.read()
    if answers1['account'] == "Christian Benitez":
        with open("cookies/cookie_2.txt", "r", encoding="utf-8") as file_cookies:
            cookies = file_cookies.read() 
    if answers['tools'] == "Quét hàng loạt":
        questions2 = [inquirer.List('list', message=f"{Fore.YELLOW}Process Speed{Fore.WHITE}", choices=['ngọc', 'vân','mua hàng',  'kiểm hàng', 'câu hỏi', 'đã gửi', 'hết hàng', 'Tag name tùy ý'],),]   
        answers2 = inquirer.prompt(questions2)
        if answers2['list'] == "Tag name tùy ý":
            a = input("Nhập tag name cần chọn:")
        else:
            a = answers2['list']
    elif answers['tools'] == "Quét theo tùy chọn":
        shortkey = input("Nhập tổ hợp phím:")
    return answers['tools'], a, cookies
   
    

def on_key_release(key):
    global need_restart, consecutive_press_count
    if key == keyboard.Key.esc:
        need_restart = True
        return False  # stop listener


last_time_pressed = 0
consecutive_press_count = 0
TIME_THRESHOLD = 1  # 2 giây

listening = True

def on_press(key):
    global last_time_pressed, consecutive_press_count, listening

    if not listening:
        return
    
    current_time = time.time()

    if key == keyboard.Key.f10:
        consecutive_press_count += 1  # Tăng số lần đếm mỗi khi nhấn F10
        last_time_pressed = current_time  # Cập nhật thời gian nhấn cuối cùng sau mỗi lần nhấn
        


def stop_listener():
    global listener
    clear_and_print("Kết thúc việc lắng nghe bàn phím!")
    listener.stop()



chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--app=https://pancake.vn")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)
# driver.set_window_size(700, 800)
driver.maximize_window()

# driver.get("https://www.facebook.com")
# Danh sách các cookie từ chuỗi bạn cung cấp

driver.get('https://pancake.vn/')

# driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/header/div[2]/button").click()
# cookie_str = input("Nhập cookies của bạn vào đây:")
global data
data, a, cookie_str = choose_tool() 

# Chuyển đổi chuỗi cookie thành danh sách các cookie và thêm chúng vào trình duyệt
for item in cookie_str.split("; "):
    if "=" in item:  # chỉ xử lý nếu item có dấu "="
        name, value = item.split("=", 1)
        cookie = {"name": name, "value": value}
        driver.add_cookie(cookie)

# Tải lại trang để áp dụng các cookie
driver.refresh()
# time.sleep(1000)
try:
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/button").click()
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/span[2]/span/span[1]/div").click()
    except:
        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]/label/span/input").click()
        except:
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[4]/label/span/input").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/button[2]").click()
    try:
        # Đợi tối đa 10 giây cho phần tử có XPath 'your_xpath_here' xuất hiện và trở nên tương tác được
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/div[1]/ul/li[6]')))
        element.click()
    except:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/div/button[1]").click()
        # print("ok")
        # Đợi tối đa 10 giây cho phần tử có XPath 'your_xpath_here' xuất hiện và trở nên tương tác được
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/div[1]/ul/li[6]')))
        element1.click()
    



except Exception as e:
    print("Có lỗi, ấn tay đoạn này nha chị")

sleep(3)
u = 0

need_restart = False
is_listening = True
def clear_and_print(msg):
    print("\r" + " " * 80 + "\r" + msg, end='', flush=True)

def selenium_process(data, need_restart):
    global consecutive_press_count
    global a
    while True:
        # print(consecutive_press_count)
        # time.sleep(5)

        # Start listening to keyboard
        # with keyboard.Listener(on_release=on_key_release) as listener1:
        if data == "Quét theo tùy chọn":
            clear_and_print('nhấn f10 để tiếp tục')
            # listener = keyboard.Listener(on_press=on_press)
            # listener.start()
            # listener.join()
            check = True
            # time.sleep(5)
            # for i in range(consecutive_press_count):
            # print(consecutive_press_count)
            # time.sleep(5)
            a = 0
            while consecutive_press_count > 0:
                # print(len(driver.find_elements(By.TAG_NAME, 'sup')))
                current_messages = len(driver.find_elements(By.TAG_NAME, 'sup'))
                new_messages = current_messages - a

                if new_messages == 0:  # Không có tin nhắn mới
                    clear_and_print(f"Vẫn chưa có tin nhắn mới, còn {consecutive_press_count} lần")
                    continue
                else:
                    # print("Đã bắt đầu")
                    try:
                        sup_elements = driver.find_elements(By.TAG_NAME, 'sup')
                        sup_elements1 = sup_elements[:-1]
                        # print(len(sup_elements1))
                        # print("Độ dài của sup_elements1", len(sup_elements1))
                        duyetqua = min(consecutive_press_count, len(sup_elements1))
                        # duyetqua = min(consecutive_press_count, len(sup_elements))
                        # print("độ dài nhỏ nhất", duyetqua)
                        # if sup_elements == 1:
                        #     duyetqua = len(sup_elements1)
                        # else:
                        #     duyetqua = len(sup_elements1) - 1
                        # duyetqua = len(sup_elements1)
                        for j in range(duyetqua):
                            first_sup = sup_elements1[j]
                            # first_sup = sup_elements[j]
                            # start_time = time.time()
                            first_sup.click()
                            # time.sleep(0.15)#0.23
                            time.sleep(delay)
                            
                            # action = ActionChains(driver)
                            # action.key_down(Keys.ALT).send_keys(f'{shortkey}').key_up(Keys.ALT).perform()
                            pyautogui.hotkey('alt', shortkey)
                            # end_time = time.time()
                            # elapsed_time = end_time - start_time
                            # print(f"Thời gian thực hiện: {elapsed_time:.4f} giây")
                            consecutive_press_count -=1
                            # a = len(driver.find_elements(By.TAG_NAME, 'sup'))
                        # print(f"Đã chạy xong lần {i} trong {consecutive_press_count} lần")
                        # consecutive_press_count -= duyetqua
                    except Exception as e:
                        check = False
                    a = len(driver.find_elements(By.TAG_NAME, 'sup'))
                    # print(a)
                    # time.sleep(2)

            
        # The code block you provided is a part of a Python script that automates certain actions on
        # a website. Specifically, it is a section that handles the "Quét hàng loạt" (Batch Scan)
        # functionality.
        elif data == "Quét hàng loạt":
            list_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'media conversation-list-item')]")
            # print(len(list_items))
            # for i in range(0, len(list_items)):
            for i in range(0, 3):

                try:
                    div = f"/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div[{i+2}]/div[3]/div/span/div"
                    checkdiv = driver.find_element(By.XPATH, div)
                except Exception as e:
                    div = f"/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div[{i+2}]/div[2]/div/span/div"
                    checkdiv = driver.find_element(By.XPATH, div)
                try:
                    if len(list_items[i].find_elements(By.TAG_NAME, "sup")) and not len(checkdiv.find_elements(By.XPATH, "./div")):
                        # print("Đã ok")
                        list_items[i].click()
                        tagnames = driver.find_elements(By.CLASS_NAME, "row_tag_list")
                        
                        if len(tagnames) == 1:
                            clear_and_print("Đã vào 1")
                            # sleep(5)
                            tagnames2 = driver.find_element(By.CLASS_NAME, "row_tag_list")
                            buttons = tagnames2.find_elements(By.TAG_NAME, "button")
                            for button in buttons:
                                button_value = button.text.lower()
                                print(button_value)
                                print(a)
                                if button_value == a:
                                    button.click()
                                    break
                        if len(tagnames) == 2:
                            clear_and_print("Đã vào 2")
                            # sleep(5)
                            tagnames2 = tagnames
                            for tagname in tagnames2:
                                buttons = tagname.find_elements(By.TAG_NAME, "button")
                                for button in buttons:
                                    button_value = button.text.lower()
                                    # print(button_value)
                                    if button_value == a:
                                        button.click()
                                        break
                        
                                
                        else:
                            tagnames2 = tagnames[1:]
                            clear_and_print("Đã vào 3")
                            # sleep(5)
                            if a == "ngọc":
                                action1 = ActionChains(driver)
                                action1.key_down(Keys.ALT).send_keys(1).key_up(Keys.ALT).perform()
                            elif a == "vân":
                                action2 = ActionChains(driver)
                                action2.key_down(Keys.ALT).send_keys(0).key_up(Keys.ALT).perform()
                        
                        
                except Exception as e:
                    print(e)
                    clear_and_print("Chụp hình lại lỗi lại cho em nhé")


            
        if need_restart:
            data, a = choose_tool()
            need_restart = False



def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_key_release) as listener:
        listener.join()

def detect_mobile_network(phone_number):
    # Lấy 3 chữ số đầu tiên của số điện thoại
    prefix = phone_number[:3]
    
    # Kiểm tra thuộc mạng nào
    if prefix in ['086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039']:
        return "Viettel"
    elif prefix in ['088', '091', '094', '081', '082', '083', '084', '085']:
        return "Vinaphone"
    elif prefix in ['089', '090', '093', '070', '079', '077', '076', '078']:
        return "Mobifone"
    elif prefix in ['092', '056', '058']:
        return "Viettel"
    elif prefix in ['099', '059']:
        return "Viettel"
    else:
        return "Unknown"


def copy_phonenb():
    # Đợi một khoảng thời gian ngắn để bạn có thể copy nội dung
    # time.sleep(5)  # Đợi 5 giây
    while True:
        try:
            phone_numbers = driver.find_element(By.CLASS_NAME, "ant-message")
            span_numbers = phone_numbers.find_element(By.TAG_NAME, "span")
            phone_number = span_numbers.find_elements(By.XPATH,"./*")
            if phone_number:
                content = pyperclip.paste()

                # api_id = 28057844
                # api_hash = 'eacbc1e2114aef8967197688de70d2db'
                with open("clipboard_content.txt", "w", encoding="utf-8") as file:
                    file.write(content)

                global nhamang

                nhamang = detect_mobile_network(content)
                
                if nhamang == "Viettel":
                    # devicesId = "2d017fbf"
                    # devicesId = "420060514f82c3a7"
                    try:
                        deviceId = getDevice(0)
                        try:
                            goi = f"adb -s {deviceId.serial} shell am start -a android.intent.action.DIAL -d tel:{content}"
                            print(goi)
                            subprocess.run(goi, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        except Exception as e:
                            clear_and_print("lỗi",e)
                        time.sleep(3)
                        click_ocr("image/call2sim.png", deviceId)
                        time.sleep(1)
                        click_ocr("image/viettel.png", deviceId)
                        checkendcall = True
                        while checkendcall:
                            if KB.is_pressed('f2'):
                                click_ocr("image/test1.png", deviceId)
                                checkendcall = False

                    except Exception as e:
                        clear_and_print("Đã vào except")
                
                elif nhamang == "Vinaphone":
                    try:
                        deviceId = getDevice(0)
                        try:
                            goi = f"adb -s {deviceId.serial} shell am start -a android.intent.action.DIAL -d tel:{content}"
                            print(goi)
                            subprocess.run(goi, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        except Exception as e:
                            clear_and_print("lỗi",e)
                        time.sleep(3)
                        click_ocr("image/call2sim.png", deviceId)
                        time.sleep(1)
                        click_ocr("image/vinaphone.png", deviceId)
                        checkendcall = True
                        while checkendcall:
                            if KB.is_pressed('f2'):
                                click_ocr("image/end2sim.png", deviceId)
                                checkendcall = False

                    except Exception as e:
                        clear_and_print("Đã vào execept")

                else:
                    try:
                        deviceId = getDevice(1)
                        try:
                            goi = f"adb -s {deviceId.serial} shell am start -a android.intent.action.DIAL -d tel:{content}"
                            print(goi)
                            subprocess.run(goi, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        except Exception as e:
                            print("lỗi",e)
                        print("ok1")
                        time.sleep(4)
                        click_ocr("image/call1sim.png", deviceId)

                        checkendcall = True
                        while checkendcall:
                            if KB.is_pressed('f2'):
                                click_ocr("image/end1sim.png", deviceId)
                                checkendcall = False



                    except Exception as e:
                        print("Đã vào exrpt")
                        print(e)
                

                time.sleep(1)
                # messages = client.get_messages('https://t.me/TempMail_org_bot')
                # for message in messages:
                #     return message.text.split("**")[1]

                

            
            # clear_and_print("Nội dung đã được lưu vào 'clipboard_content.txt'.")
        except Exception as e:
            # print(e)
            # print("Chưa có nội dung copy")
            pass
            
# api_id = 28057844
# api_hash = 'eacbc1e2114aef8967197688de70d2db'

# client = TelegramClient('session_name', api_id, api_hash)
# client.start()

# client.send_message('https://t.me/TempMail_org_bot', 'Hello, myself!')   


copy_thread = Thread(target=copy_phonenb)
copy_thread.start()

keyboard_thread = Thread(target=start_keyboard_listener)
keyboard_thread.start()

selenium_thread = Thread(target=selenium_process, args=(data, need_restart))
selenium_thread.start()

selenium_thread.join()  # Chờ cho 
