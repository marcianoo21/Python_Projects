from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(60)

        down_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed = self.driver.find_element(By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"Download speed: {down_speed.text} Mb/s")
        print(f"Upload speed: {up_speed.text} Mb/s")



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
