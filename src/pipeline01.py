import requests
import time
from tinydb import TinyDB
from datetime import datetime

def extract_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    dados = response.json()
    return dados


def transform_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().timestamp()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }

    return dados_transformados

def salvar_dados_tinydb(dados, db_name="biticoin_json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print(f"Dados salvos com sucesso em {db_name}")


if __name__ == "__main__":
    #extracao de dados
    while True: 
        dados_jason = extract_dados_bitcoin()
        #transformacao de dados
        dados_transformados = transform_dados_bitcoin(dados_jason)
        #salvamento de dados
        salvar_dados_tinydb(dados_transformados)
        time.sleep(15)

