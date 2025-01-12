import requests
import time
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, Bitcoin

# Add database connection
engine = create_engine('sqlite:///bitcoin.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

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

def salvar_dados_sql(dados):
    session = Session()
    bitcoin = Bitcoin(
        valor=float(dados["valor"]),
        criptomoeda=dados["criptomoeda"],
        moeda=dados["moeda"]
    )
    session.add(bitcoin)
    session.commit()
    session.close()
    print("Dados salvos com sucesso no SQLite")


if __name__ == "__main__":
    #extracao de dados
    while True: 
        dados_jason = extract_dados_bitcoin()
        #transformacao de dados
        dados_transformados = transform_dados_bitcoin(dados_jason)
        #salvamento de dados
        salvar_dados_sql(dados_transformados)
        time.sleep(15)

