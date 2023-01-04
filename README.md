# webscraping
Extracción de información de webscraper.io, datos guardados en .csv y mostrados en una vista.

Para realizar el "raspado" de la página web: https://webscraper.io/test-sites/e-commerce/scroll/  

Se creó un script en python llamado scraper.py, en el cual se accede a las 3 urls correspondientes a las diferentes categorías de dispositivos:  
para computers, laptops y tablets y para phones, touch.  
Haciendo uso de la librería de Selenium se accede al navegador y con Beautiful Soup, la librería que permite que con web scraping  
se atraviese el DOM (modelo de objeto de documento), de manera que con ambas se realiza scraping de páginas dinámicas,  
como es el caso del website en cuestión, el cual carga más información a medida que se hace scroll.

Este scraping tiene siguientes características:

●	Extrae un listado con la información de los productos.
●	Guarda  la información de los productos en un archivo .cvs
●	Muestra los datos en una vista.

Todo esto se hizo dentro de un ambiente virtual env utilizando el microframework Flask.

