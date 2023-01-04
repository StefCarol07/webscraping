from flask import Flask, render_template
from webscraping.scraper import obtener_productos


app = Flask(__name__)

@app.route("/")
def scraper():
    lista_productos = obtener_productos()
    return render_template('scraper.html', datos_productos = lista_productos)

