'''
Created on 1 ago. 2017
@author: JLVEGA
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('skeleton.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/noticias')
def noticias():
    return render_template('noticias.html')


@app.route('/asignaturas')
def asignaturas():
    return render_template('asignaturas.html')


@app.route("/test")
def test():
    app.logger.info("Servicio test")
    return "Test de lanzamiento"


if __name__ == '__main__':
    app.run(port=8889)
