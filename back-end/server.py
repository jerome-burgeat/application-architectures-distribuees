import os
import sys, Ice
import ApplicationArchitecturesDistribuees
import pymongo
import json
from mutagen.mp3 import MP3
 
class Server(ApplicationArchitecturesDistribuees.Server):

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydb"]
    collection = db["musics"]
    
    def __init__(self):
        self.index = 0
        self.uploadingFiles = {}

    def helloWorld(self, helloWorld, current=None):
        print(helloWorld)
        
    def getNewIndex(self, current=None):
        index = self.index
        self.index += 1
        return index
       
    def uploadPart(self, id, part, current=None):
        if id not in self.uploadingFiles : self.uploadingFiles[id] = b""
        self.uploadingFiles[id] += part
        return 0
        
    def uploadFileAndInsertMusic(self, id, filename, current=None):
        print("upload file ... ")
        file = open("musics/" + filename, "wb")
        file.write(self.uploadingFiles[id])
        file.close()
        # fd = file.fileno()
        # print("file infos: " , os.stat("musics/" + filename).st_file_attributes)
        audio = MP3("musics/" + filename)
        artist = audio['TPE1'].text[0] if 'TPE1' in audio else None
        title = audio['TIT2'].text[0] if 'TIT2' in audio else None
        album = audio['TALB'].text[0] if 'TALB' in audio else None
        print("file infos: " , title, album, artist)
        print("upload file successfuly! ")
        musicData = '{"title": "' + title + '", "artist": "' + artist + '", "album": "' + album + '", "url": ' + '"musics/' + filename + '"}'
        dataToInsert = json.loads(musicData)
        result = self.collection.insert_one(dataToInsert)
        # print("result: " + result)
        return 0

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