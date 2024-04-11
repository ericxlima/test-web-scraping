from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import json


# Inicializar o Chrome
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# Resto do seu código de automação...
# entrar no site das tartarugas: https://www.scrapethissite.com/pages/frames/
link = "https://www.scrapethissite.com/pages/frames/"
driver.get(link)

# acessar o iframe
sleep(2)
iframe = driver.find_element(By.XPATH, "//iframe[@id='iframe']")
driver.switch_to.frame(iframe)
driver.find_elements(By.XPATH, "//h3[@class='family-name']")[0].text

# pegar todos os links das tartarugas
tartarugas = driver.find_elements(By.XPATH, "//div//div[@class='col-md-4 turtle-family-card']//a")
turtles_links = [turtle.get_attribute("href") for turtle in tartarugas]

turtles_data = []
# entrar no link
for link in turtles_links:
    driver.get(link)
    # sleep(1)

    # extrair foto, nome e descricao da tartaruga
    img = driver.find_element(By.XPATH, "//div[@class='col-md-6 col-md-offset-3 turtle-family-detail']//img").get_attribute("src")
    name = driver.find_element(By.XPATH, "//div[@class='col-md-6 col-md-offset-3 turtle-family-detail']//h3").text
    description = driver.find_element(By.XPATH, "//div[@class='col-md-6 col-md-offset-3 turtle-family-detail']//p").text

    turtles_info = {
        "img": img,
        "name": name,
        "description": description
    }

    turtles_data.append(turtles_info)


json_filename = "turtle.json"
with open(json_filename, "w") as json_file:
    json.dump(turtles_data, json_file, indent=4)


