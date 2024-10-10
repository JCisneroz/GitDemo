from selenium import webdriver
import time
#Chrom driver
from selenium.webdriver.chrome.service import Service
#--Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# [Cucumber - 1 Kg, Raspberry - 1/4 Kg, Strawberry - 1/4 Kg]

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


#Sum Valiation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = int (driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert totalAmount == sum


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

promo = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promo)

assert "Code applied ..!" in promo







