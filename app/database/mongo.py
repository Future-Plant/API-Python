from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient("mongodb+srv://felslender:Felslender18@cluster0.8t0lzmv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=ca)
db = client['iot_db']

