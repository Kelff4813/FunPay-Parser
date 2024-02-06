from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time


options = webdriver.FirefoxOptions()
options.add_argument('--log-level=3')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get(f'https://funpay.com/users/1724531/')
names = driver.find_elements(By.CLASS_NAME, 'tc-desc-text')
prices = driver.find_elements(By.CLASS_NAME, 'tc-price')
result = {}
pr = []

for i, p in zip(names, prices[1:]):
    name = i.text
    if 'brawlers' in name:
        info = name.split(',')
        price = int(p.text[0:-2].replace(' ', ''))
        coups = int(name.split(',')[-2].split()[-1])
        brawlers = int(name.split(',')[-1].split()[-1])
        result[coups / price] = [round(price * 0.714), coups, brawlers]
        pr.append(coups / price)
 
for i in sorted(pr, reverse=True):
    print(*result[i])
    
driver.quit()