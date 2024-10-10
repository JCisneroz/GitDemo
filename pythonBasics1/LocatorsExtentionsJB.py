from selenium import webdriver
import time

#Chrom driver
from selenium.webdriver.chrome.service import Service
#--Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") #form/div[1]/input el numero indica la opcion no.1 del formulario
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Hello@1234") #CSSSelector se usa el # y el id del elemento
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)