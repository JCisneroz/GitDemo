from selenium import webdriver #Llama a selenium
from selenium.webdriver.chrome.service import Service #se crea un objeto
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Las rutas deben escribirse con diagonales normales
service_obj = Service("C:/Users/jorge/Downloads/chromedriver-win64/chromedriver-win64/chromedriver") #Se declara el objeto

driver = webdriver.Chrome(options=options,service=service_obj) #manda llamar al objeto (chrome driver)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com") #Para llamar a la pagina (URL)
driver.get("https://www.rahulshettyacademy.com/#/practice-project")
print(driver.title) #Te regresa el titulo de la pagina
print(driver.current_url) #Te regresa el URL de la pagina
driver.get("https://www.rahulshettyacademy.com/#/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()#Cierra la pagina
