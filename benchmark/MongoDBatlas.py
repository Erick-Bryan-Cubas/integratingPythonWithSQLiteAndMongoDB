import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from configparser import ConfigParser

def connect_to_mongodb(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def create_database_collections(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    database_name = 'banco_dio'
    collections = ['cliente', 'conta']

    if database_name in client.list_database_names():
        print(f"The database '{database_name}' already exists.")
        return

    db = client[database_name]
    for collection in collections:
        if collection in db.list_collection_names():
            print(f"The collection '{collection}' already exists.")
        else:
            db.create_collection(collection)
            print(f"The collection '{collection}' has been created.")

    # Add fields to 'cliente' collection
    cliente_collection = db['cliente']
    cliente_collection.create_index('id', unique=True)
    cliente_collection.create_index('cpf', unique=True)
    cliente_collection.create_index('nome')
    cliente_collection.create_index('endereco')

    # Add fields to 'conta' collection
    conta_collection = db['conta']
    conta_collection.create_index('id', unique=True)
    conta_collection.create_index('id_cliente')
    conta_collection.create_index('tipo')
    conta_collection.create_index('agencia')
    conta_collection.create_index('num')
    conta_collection.create_index('saldo')

    print(f"The database '{database_name}' and collections have been created.")

def main():
    userprofile = os.environ['USERPROFILE']
    filepath = userprofile + '\\credenciais\\mongodbatlas.ini'
    config = ConfigParser()
    config.read(filepath)

    username = config['MONGODBATLAS']['username']
    passwd = config['MONGODBATLAS']['passwd']

    uri = f"mongodb+srv://{username}:{passwd}@clusterpython.5d4e3cz.mongodb.net/?retryWrites=true&w=majority"

    connect_to_mongodb(uri)
    create_database_collections(uri)

if __name__ == '__main__':
    main()
