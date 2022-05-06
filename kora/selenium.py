# install chromium, its driver, and selenium
import os
os.system('apt update')
os.system('apt install chromium-chromedriver')
os.system('pip install selenium')
# set options to be headless, ..
from selenium.webdriver import Chrome, ChromeOptions
options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# create a webdriver instance, ready to use
wd = Chrome('chromedriver',options=options)

# make it easier to query and explore elements
from selenium.webdriver.remote.webelement import WebElement
WebElement.__str__ = lambda self: self.get_attribute('outerHTML')
WebElement.__repr__ = WebElement.__str__
Chrome.select = WebElement.select = lambda self, v: self.find_elements('css selector', v)
Chrome.select1 = WebElement.select1 = lambda self, v: self.find_element('css selector', v)
WebElement.__getitem__ = WebElement.get_attribute

# show screenshot easily with _repr_png_
def _screen_shot(self):
    from tempfile import NamedTemporaryFile as TempFile
    tmp = TempFile(suffix='.png')
    self.save_screenshot(tmp.name)
    return tmp.read()
Chrome._repr_png_ = _screen_shot
