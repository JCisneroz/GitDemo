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


driver.get ("https://www.liverpool.com.mx/")
driver.maximize_window()
#Seleccionando producto
driver.find_element(By.ID, "mainSearchbar").send_keys("linea blanca")
driver.find_element(By.CSS_SELECTOR, ".icon-zoom").click()
driver.find_element(By.XPATH, "//h3[contains(text(),'Refrigerador dúplex Hisense 22 pies cúbicos tecnol')]").click()
driver.find_element(By.XPATH, "//button[@id='opc_pdp_addCartButton']").click()
#driver.find_element(By.XPATH, "//button[normalize-space()='No, gracias']").click()
ProductoAgregado = driver.find_element(By.XPATH, "//div[contains(text(),'Agregaste un producto a tu bolsa')]").text
assert "Agregaste un producto a tu bolsa" in ProductoAgregado
print(ProductoAgregado)
driver.find_element(By.CSS_SELECTOR, "button[class='a-header__bag'] span").click()

#ComprobandoTotales
subTotal = driver.find_element(By.XPATH, "//p[normalize-space()='$32,999.00']").text
total = driver.find_element(By.XPATH, "//p[@class='a-inlineElement a-inlineElement--enphasis a-inlineElement--total -enphasisDecimal -alignDecimal']").text
descuento = driver.find_element( By.XPATH, "//p[normalize-space()='$15,839.52']" ).text
print("Subtotal", subTotal)
print("Descuento", descuento)
print("Total (IVA incluido)", total)
def convertir (subTotal):
    subTotal = ('$, ""')
    total = ('$, ""')
    return float

assert subTotal > total
print("Descuento OK")

#Eligiendo Ciudad
driver.find_element(By.CSS_SELECTOR, "span[class='m-navDesktop__selectstore'] span[class='ml-1']").click()
driver.find_element(By.XPATH, "//div[@class='d_select_store']//button[1]").click()
driver.find_element(By.XPATH, "//input[@id='CP']").send_keys("culiacan")
driver.find_element(By.XPATH, "//button[@class='mdc-button a-btn__primary m-eddBox__updateButton']").click()
driver.find_element(By.XPATH, "//input[@id='store-46']").click()
tiendaSeleccionada = driver.find_element(By.CSS_SELECTOR, "span[class='m-navDesktop__selectstore'] span[class='selected_Store ml-1']").text
assert "Liverpool Culiacán" in tiendaSeleccionada
print("Tienda seleccionada correctamente")


time.sleep(2)