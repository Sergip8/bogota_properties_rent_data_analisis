from pymongo import MongoClient
import pandas as pd

def connect_to_mongo(db_name, collections):
    """
    Conecta a una base de datos MongoDB y devuelve los datos de las colecciones en un DataFrame.
    """

    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]

    data = []
    for collection in collections:
        collection_data = list(db[collection].find())
        data +=collection_data
        
    
    df = pd.json_normalize(data, sep='_')       

    return df
