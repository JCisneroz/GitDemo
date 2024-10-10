from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5) # Este agregara una pausa en cada linea de codigo
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText





