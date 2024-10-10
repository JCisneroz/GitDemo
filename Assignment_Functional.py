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

#Expectedlist&Click in different buttons
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']#La lista se debe colocar cada elemento con ''
actualList = []
print(expectedList)
results = driver.find_elements(By.XPATH, "//div [@class='products']/div") #Se puede usar el mismo path
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text) # "h4"Aqui solo se agrega la division que continua para los nombres de la lista
    result.find_element(By.XPATH, "div/button").click() #Aqui se le da click al boton de "ADD TO CART"
assert expectedList == actualList #Aqui compara que los datos de la lista obtenida sean iguales a los de la pagina

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


#Sum Valiation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print("totalAmount",sum)
totalAmount = int (driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert totalAmount == sum

#Inserting promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
promo = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promo)

discountedAmount = float (driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalAmount > discountedAmount
print("TotalAmount is ok")
assert "Code applied ..!" in promo

