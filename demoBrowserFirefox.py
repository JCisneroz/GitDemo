from selenium import webdriver #Llama a selenium
from selenium.webdriver.firefox.service import Service #se crea un objeto
from selenium.webdriver.firefox.options import Options


#Las rutas deben escribirse con diagonales normales
options = Options()
service_obj = Service("C:/Users/jorge/Downloads/geckodriver-v0.35.0-win64/geckodriver.exe") #Se declara el objeto
driver = webdriver.Firefox(service=service_obj, options=options) #manda llamar al objeto (chrome driver)

driver.maximize_window()
driver.get("https://www.liverpool.com.mx") #Para llamar a la pagina (URL)
driver.get("https://www.liverpool.com.mx/tienda/hombre/catst40855192")
print(driver.title) #Te regresa el titulo de la pagina
print(driver.current_url) #Te regresa el URL de la pagina
driver.get("https://www.liverpool.com.mx/tienda/hombre/catst40855192")
#driver.minimize_window()
driver.back() 
driver.refresh()
driver.forward()
driver.close()#Cierra la pagina