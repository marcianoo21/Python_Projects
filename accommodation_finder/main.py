import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = "https://appbrewery.github.io/Zillow-Clone/" # set to the San Francisco area

headers = {
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8,fr;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

response = requests.get(url, headers)
zillow_web = response.text
soup = BeautifulSoup(zillow_web, "html.parser")
links_a = soup.find_all(name='a', class_="property-card-link")
links = [link.get('href') for link in links_a]
#print(links)

prices_span = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
prices = [price.text.split('+')[0].split('/mo')[0] for price in prices_span]
#print(prices)

addresses = soup.find_all(name='address')
formatted_addresses = [address.text.strip().replace('|', '') for address in addresses]
#print(formatted_addresses)

driver = webdriver.Chrome()
#time.sleep(5)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdxI6swS8TxHtDGXVHVfTJJ44vp2P9e_7rJ6r3nOeipA-vOGg/viewform?usp=sf_link")

for i in range(len(formatted_addresses)):
    first_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    first_input.send_keys(formatted_addresses[i])
    #time.sleep(1)

    second_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    second_input.send_keys(prices[i])
    #time.sleep(1)

    second_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    second_input.send_keys(links[i])
    #time.sleep(1)

    send_button = driver.find_element(By.XPATH, value = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_button.click()
    time.sleep(2)
    
    send_again = driver.find_element(By.XPATH, value = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_again.click()
    time.sleep(1)

#driver.quit()