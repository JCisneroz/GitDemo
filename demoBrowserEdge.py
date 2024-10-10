from selenium import webdriver #Llama a selenium
from selenium.webdriver.edge.service import Service #se crea un objeto
#options = webdriver.edge.options()
#options.add_experimental_option("detach", True)

#Las rutas deben escribirse con diagonales normales
service_obj = Service("C:/Users/jorge/Downloads/edgedriver_win64 (2)/msedgedriver") #Se declara el objeto
driver = webdriver.Edge(service=service_obj) #manda llamar al objeto (chrome driver)


driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com") #Para llamar a la pagina (URL)
driver.get("https://www.rahulshettyacademy.com/#/practice-project")
print(driver.title) #Te regresa el titulo de la pagina
print(driver.current_url) #Te regresa el URL de la pagina
driver.get("https://www.google.com")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
#driver.close()#Cierra la pagina