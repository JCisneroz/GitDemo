from selenium import webdriver
import time
#Chrom driver
from selenium.webdriver.chrome.service import Service
#--Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5) # Este agregara una pausa en cada linea de codigo



driver.get ("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #Este time.sleep se debe conservar porqué en la siguiente linea esta extrayendo una lista y sino se le da el tiempo, la prueba falla
results = driver.find_elements(By.XPATH, "//div [@class='products']/div") #list[]
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()


driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

promo = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promo)

assert "Code applied ..!" in promo





