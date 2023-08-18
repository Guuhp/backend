from pymongo.mongo_client import MongoClient
from datetime import datetime


URI = "mongodb+srv://mauriciobatista:GmwZRJ3UDkUrgnZv@snapcut.kzunty0.mongodb.net/?retryWrites=true&w=majority"
CLIENT = MongoClient(URI)


try:
    CLIENT.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


DATABASE = CLIENT['snapcut']
COLLECTION = DATABASE["Users"]


class User:
    def __init__(self, username, email, password, bio) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.bio = bio
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        self.videos = []
        self.friends = []


user_1 = User("root", "root@gmail.com", "admin", "oi sou o root")
user_2 = User("admin", "admin@gmail.com", "root", "oi sou o admin")

# COLLECTION.insert_many([vars(user_1), vars(user_2)])
