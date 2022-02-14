from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

URL = "https://www.instagram.com/"

USERNAME = ""
PASSWORD = ""

chrome_driver_path = "C:/Users/HP/PycharmProjects/chromedriver"
ACCOUNT = "Name of the person"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
time.sleep(6)
username = driver.find_element_by_name("username")
username.send_keys(USERNAME)
password = driver.find_element_by_name("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(6)
not_now1 = driver.find_element_by_class_name("cmbtv")
not_now1.click()
time.sleep(4)
not_now2 = driver.find_element_by_class_name("HoLwm")
not_now2.click()
time.sleep(4)
search = driver.find_element_by_class_name("eyXLr")
search.click()
time.sleep(4)
name = driver.find_element_by_class_name("DljaH")
name.send_keys(ACCOUNT)
time.sleep(5)
account = driver.find_element_by_class_name("-qQT3")
account.click()
time.sleep(4)
message = driver.find_element_by_class_name("T0kll")
message.click()
time.sleep(4)
text = driver.find_element_by_class_name("ItkAi")
# text.send_keys("Hey")
text.click()
time.sleep(5)
msg = driver.find_element_by_tag_name("textarea")
msg.send_keys("Message to be send")
msg.send_keys(Keys.ENTER)

