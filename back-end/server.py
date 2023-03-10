import sys, Ice
import ApplicationArchitecturesDistribuees
import pymongo
import json
 
class Server(ApplicationArchitecturesDistribuees.Server):

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydb"]
    collection = db["test"]

    def helloWorld(self, helloWorld, current=None):
        print(helloWorld)

    def addMusic(self, dataMusic:str, current=None):
        # data = {"title": "test", "url": "www.goggle.com"}
        dataToInsert = json.loads(dataMusic)
        result = self.collection.insert_one(dataToInsert)

    def deleteMusic(self, titleMusic:str, current=None):
        result = self.collection.delete_one({"title": titleMusic})

    def searchMusic(self, titleMusic:str, current:None):
        result = self.collection.find_one({"title": titleMusic})
        print(result)

    def updateMusicChangeTitle(self, titleCurrent:str, newTitle:str, current=None):
        result = self.collection.update_one({"title": titleCurrent}, {"$set": {"title": newTitle}})
 
with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ApplicationArchitecturesDistribuees", "default -p 10000")
    object = Server()
    adapter.add(object, communicator.stringToIdentity("ApplicationArchitecturesDistribuees"))
    adapter.activate()
    communicator.waitForShutdown()