from flask import Flask
import random

app = Flask(__name__)

facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
              "La adiccion tecnologica puede afectar a personas de todas las edades, desde niños hasta mayores", 
              "Esta demostrado que la adiccion tecnologica provoca efectos negativos en la salud tanto mental como fisica"]

moneda_list = ["cara","cruz"]

@app.route("/")

def index():
    return f'<h1>Hola, esta es una pagina hecha con flask</h1> <a href="/random_fact">¡Ver un dato aleatorio!</a> <a href="/moneda">¡Moneda!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'
 

@app.route("/moneda")
def moneda():
    return f'<p>{random.choice(moneda_list)}</p>'
app.run(debug=True)
