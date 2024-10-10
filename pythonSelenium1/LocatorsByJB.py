from selenium import webdriver
import time

#Chrom driver
from selenium.webdriver.chrome.service import Service
#--Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get ("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Formas de llamar a los localizadores ID, CSSSelector, Class name, Name, Linktext

#ID
driver.find_element(By.NAME, "name").send_keys("Jorge Cisneros") #por "name"
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com") #Por "name"
driver.find_element(By.ID, "exampleInputPassword1").send_keys("DONGATO123") #Por ID
driver.find_element(By.ID, "exampleCheck1").click()

#Xpath //tagname[@attribute='value'] -> //input[@type='submit']
#CSS -  tagname[attribute='value'] -> //input[@type='submit'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


#Stactic dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1) #se puede encontrar por numero comienza del 0
dropdown.select_by_visible_text("Male") #Se puede encontrar por texto
#dropdown.select_by_value("value") #Se puede encontrar por "value"

driver.find_element(By.XPATH, "//input[@type='date']").send_keys("03/07/1993")




driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)



assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hola de new")







time.sleep(5)
