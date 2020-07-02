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

# make it easier to query and explore elements
wd.select = wd.find_elements_by_css_selector
wd.select1 = wd.find_element_by_css_selector
from selenium.webdriver.remote.webelement import WebElement
WebElement.__str__ = lambda self: self.get_attribute('outerHTML')
WebElement.__repr__ = WebElement.__str__
