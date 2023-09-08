import time

from selenium import  webdriver
from  selenium.webdriver.common.by import By
class FileUpload():
    def file_uploading(self):
        baseUrl="https://www.plupload.com/examples/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        element=driver.find_element(By.XPATH,"//input[@type='file']")
        element.send_keys("C:\\Users\\Daya\\Desktop\\mr.jpg")

        time.sleep(3)


ob=FileUpload()
ob.file_uploading()

