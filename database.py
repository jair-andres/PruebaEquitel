from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://JAIR787:password@cluster0.ibtchgl.mongodb.net/test'
ca = certifi.where()

def dbConnection():
    try:
        cliente = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = cliente["development_test"]
    except ConnectionError:
        print('Error de conexion con la bdd')
    return db