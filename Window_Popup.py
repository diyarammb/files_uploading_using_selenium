import time
from selenium import  webdriver
from  selenium.webdriver.common.by import By
from pynput.keyboard import Key,Controller

class FileUploadWindow():
    def WindowPopUp(self):
        baseUrl="https://www.plupload.com/examples/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//input[@type='file']").click()
        # element.click()
        time.sleep(3)
        Keyboard=Controller()
        Keyboard.type("C:\\Users\\Daya\\Desktop\\mr.jpg")
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)


ob=FileUploadWindow()
ob.WindowPopUp()

