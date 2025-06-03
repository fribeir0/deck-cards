import requests
import time
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return cards()

@app.route("/cards", methods=["GET"])
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
def latency(ms:int) :
    print (f"aguardando: {ms}")
    time.sleep(ms)
    return dict(message=f"Esta pagina ira recarregar")

if __name__ == "__main__" :
    app.run(host="127.0.0.1",port="9000")