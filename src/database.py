from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, Integer, String,DateTime
from datetime import datetime

Base = declarative_base()

class BitcoinPreco(Base):
    __tablename__ = "bitcoin_precos"
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(50), nullable=False)
    moeda = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

   