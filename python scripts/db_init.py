from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import Bundle
import pymysql

engine = create_engine('mysql+pymysql://root:Pass2546@34.138.14.68/speakme_data', echo=True)
meta = MetaData()

users = Table('users', meta,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('username', String(15), unique=True),
              Column('password', String(15)),
              Column('language', String(2))
              )

chat_logs = Table('chat_logs', meta,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('user_id_1', Integer, ForeignKey('users.id'), nullable=False),
                  Column('user_id_2', Integer, ForeignKey('users.id'), nullable=False)
                  )

messages = Table('messages', meta,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('message', String(1000)),
                 Column('date', DateTime),
                 Column('sender_id', Integer, ForeignKey('users.id'), nullable=False),
                 Column('recipient_id', Integer, ForeignKey('users.id'), nullable=False)
                 )

meta.create_all(engine)


