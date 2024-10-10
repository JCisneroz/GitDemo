import time
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
#print(len(checkboxes))


for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

#dropdown
driver.find_element(By.ID, "dropdown-class-example").click()
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option3")



radiobuttons = driver.find_elements(By.NAME, "radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#radiobuttons = driver.find_elements_by_name("radioButton")
#radiobuttons[2].click()
#assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text" ).is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


#assert driver.find_element_by_id("displayed-text").is_displayed()
#driver.find_element_by_id("hide-textbox").click()
#assert not driver.find_element_by_id("displayed-text").is_displayed()



time.sleep(10)
