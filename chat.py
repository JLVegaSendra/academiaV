'''
Created on 1 ago. 2017
@author: usuario
'''

from jinja2 import Template
from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="../src/")


@app.route('/')
def index():
    return render_template('./templates/skeleton.html')


@app.route('/contacto')
def contacto():
    return render_template('./templates/contacto.html')


@app.route('/historia')
def historia():
    return render_template('./templates/historia.html')


@app.route('/noticias')
def noticias():
    return render_template('./templates/noticias.html')


@app.route('/asignaturas')
def asignaturas():
    return render_template('./templates/asignaturas.html')


@app.route("/test")
def test():
    app.logger.info("Servicio test")
    return "Test de lanzamiento"


if __name__ == '__main__':
    app.run(port=80)
