# install chromium, its driver, and selenium
import os
os.system('apt install chromium-chromedriver')
os.system('pip install selenium')
# set options to be headless, ..
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# create a webdriver instance, ready to use
wd = webdriver.Chrome('chromedriver',options=options)