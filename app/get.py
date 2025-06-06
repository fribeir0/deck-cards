import requests

#def get_cards () :
   # cards=requests.get("http://35.153.211.157:9000/cards", timeout=15)
def get_health (x) :
    try:
        health=requests.get("http://35.153.211.157:9000/health", timeout=x)
        print ("sucess")
    except requests.RequestException as r:
        print ("erro na requisicao",r)

def get_404 (x):
    try:
        errors=requests.get("http://35.153.211.157:9000/404",timeout=x)
        print("succes")
    except requests.RequestException as r:
        print ("erro na requisicao",r)
if __name__ == "__main__" :
    for i in range (0,1000) :
       # get_cards()
        get_404(1)
        get_health(1)
        print("requisicoes",i)