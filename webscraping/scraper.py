from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from csv import writer


url_laptops = 'https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops'
url_tablets = 'https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets'
url_phones = 'https://webscraper.io/test-sites/e-commerce/scroll/phones/touch'

urls = [url_laptops, url_tablets, url_phones]
nombre_producto = ['laptops', 'tablets', 'phones']

todos_productos = {}


def obtener_productos():

    s = Service('C:/Program Files (x86)/chromedriver.exe')

    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])


    driver = webdriver.Chrome(options=options, service=s)

    for i in range(0, len(urls)):

        driver.get(urls[i]) 

        ultima_alt = driver.execute_script("return document.body.scrollHeight")

        while True:

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            sleep(0.3)

            nueva_alt = driver.execute_script("return document.body.scrollHeight")

            if ultima_alt == nueva_alt:
                    break
            ultima_alt = nueva_alt
                
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        sleep(1)

        productos = []

        for caption in soup.find_all(class_='caption'):

                nombre = caption.find(class_='title').text
                descripcion = caption.find(class_='description').text
                precio = caption.find(class_='pull-right price').text

                for ratings in soup.find_all(class_='ratings'):

                    reviews = ratings.find(class_='pull-right').text  

        
                info_producto = [nombre, descripcion, precio, reviews]
                productos.append(info_producto)
        
        todos_productos[nombre_producto[i]] = productos

        with open( nombre_producto[i] + '.csv' , 'w' , encoding='utf8', newline='') as file:
            thewriter = writer(file)
            encabezado = ['Nombre producto', 'Descripcion', 'Precio', 'Reviews']
            thewriter.writerow(encabezado)

            thewriter.writerows(productos)

    return todos_productos



