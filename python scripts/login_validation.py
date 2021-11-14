from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pymysql

engine = create_engine('mysql+pymysql://root:Pass2546@34.138.14.68/speakme_data', echo=True)

