import sqlalchemy as db
import getpass
import json
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

url= os.getenv('PASSWORD')
engine = db.create_engine(url)
connection = engine.connect()


def addEmo(idvideo,pred):
    query = """INSERT INTO `emotions` (idvideo, angry, disgust, fear, happy, sadness, surprise, time) 
        VALUES ({},{},{},{},{},{},{}, CURRENT_TIMESTAMP);""".format(idvideo,pred[0], pred[1], pred[2], pred[3], pred[4], pred[5])
    connection.execute(query) 
    return "Ok!"

def getData(idvideo):
    query = """
        SELECT angry,disgust,fear,happy,sadness,surprise FROM emotions WHERE idVideo='{}'
    """.format(idvideo)
    df= pd.read_sql_query(query, engine)
    return df

