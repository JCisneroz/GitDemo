import time
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.makemytrip.com/")
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']" ).send_keys("del")
time.sleep(2)
cities = driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
print (len(cities))
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break

driver.find_element(By.XPATH, "//p[text()='Delhi, India']").click()
#driver.find_element_by_xpath("//p[text()='Delhi, India']").click()



