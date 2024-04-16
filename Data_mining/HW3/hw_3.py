import pymongo
import json

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Создание базы данных
database_name = "homework_3"
database = client[database_name]

# Создание коллекции и загрузка данных из файла JSON
collection_name = "books_toscrape"
collection = database[collection_name]

# Чтение данных из файла JSON
with open("books_data.json", encoding='utf-8') as file:
    data = json.load(file)

# Вставка данных в коллекцию
collection.insert_many(data)

# Закрытие соединения с MongoDB
client.close()
