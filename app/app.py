import requests
import time
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/", methods=["GET"])
def index():
    return cards()

@app.route("/cards", methods=["GET"])
@metrics.counter("cards-requests","Numero de cards solicitados")
def cards () :
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    cartas = response.json()
    deck_id = cartas["deck_id"]
    image_list = []

    for i in range (0,14) :
        req = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2")
        png = req.json()
        image = png["cards"][0]["image"]
        image_list.append(image)
    html_template=""
    for x in range (0,9):
        html_template += f'<img src="{image_list[x]}">\n'
    return html_template


@app.route ("/latency/<int:ms>", methods=["GET"])
@metrics.gauge("latency", "latencia em milisegundos (simulação)")
def latency(ms:int) :
    print (f"aguardando: {ms}")
    time.sleep(ms)
    return dict(message=f"Esta pagina teve uma latencia de {ms} ms")
@app.route ("/404", methods=["GET"])
def erro404 () :
    response = requests.get("http://google.com.br")
    return dict (message="ERROR", status_code=response.status_code), 404
@app.route ("/health", methods=["GET"])
def health() :
    response = requests.get("http://google.com.br")
    return dict (message="SUCCESS", status_code=response.status_code)

if __name__ == "__main__" :
    app.run(host="127.0.0.1",port="9000")