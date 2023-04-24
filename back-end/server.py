import os
import sys, Ice
import ApplicationArchitecturesDistribuees
import pymongo
import json
import vlc
from mutagen.mp3 import MP3
import Levenshtein
 
class Server(ApplicationArchitecturesDistribuees.Server):

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydb"]
    collection = db["musics"]
    
    def __init__(self):
        self.ipv4 = "192.168.1.128"
        self.index = 0
        self.uploadingFiles = {}
        self.player = vlc.Instance()
        self.media_player = self.player.media_player_new()

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
        # musicData = '{"title": "' + title + '", "artist": "' + artist + '", "album": "' + album + '", "url": ' + '"musics/' + filename + '"}'
        musicData = '{"title": "' + title + '", "artist": "' + artist + '", "album": "' + album + '", "filename": "' + filename + '", "url": ' + '"E://Yingqi/etudes/M1S2/application-architectures-distribuees/back-end/musics/' + filename + '"}'
        dataToInsert = json.loads(musicData)
        result = self.collection.insert_one(dataToInsert)
        # print("result: " + result)
        return 0

    def getAllMusics(self, current=None):
        listMusic = []
        all_data = list(self.collection.find())
        for data in all_data:
            listMusic.append(data['title'])
        return listMusic

    def deleteMusic(self, titleMusic:str, current=None):
        result = self.collection.delete_one({"title": titleMusic})

    def searchClosestMusic(self, titleMusic:str, current=None):
        musicList = self.getAllMusics()
        min_distance = float("inf")
        closest_music = ""
        for string in musicList:
            distance = Levenshtein.distance(titleMusic, string)
            if distance < min_distance:
                min_distance = distance
                closest_music = string
        return closest_music

    def updateMusicChangeTitle(self, titleCurrent:str, newTitle:str, current=None):
        result = self.collection.update_one({"title": titleCurrent}, {"$set": {"title": newTitle}})

    def playMusic(self, musicStr, current=None):
        print("get request ! ")
        musicTitle = self.searchClosestMusic(musicStr)
        if(self.media_player.get_state() == vlc.State.Paused):
            print("music playing....")
            self.media_player.play()
            return True
        else:
            print("not music playing....")
            filter = {'title': musicTitle} 

            document = self.collection.find_one(filter)
            filename = document['filename']

            file = "musics/" + filename
            if os.path.exists(file) != True : return False
            media = self.player.media_new(file)

            media.add_option(":sout=#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:rtp{sdp=rtsp://" + self.ipv4 + "/}")
            media.add_option("--no-sout-all")
            media.add_option("--sout-keep")
            media.get_mrl()

            self.media_player = self.player.media_player_new()
            self.media_player.set_media(media)
            self.media_player.play()
            return True

    def stopMusic(self, current=None):
        if (self.media_player.is_playing()):
            self.media_player.stop()
            return True
        else: 
            return False

    def pauseMusic(self, current=None):
        if(self.media_player.is_playing()):
            print("is playing...")
            self.media_player.pause()
            return True
        else:
            print("not music playing...")
            return False
 
with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ApplicationArchitecturesDistribuees", "default -p 10000")
    object = Server()
    adapter.add(object, communicator.stringToIdentity("ApplicationArchitecturesDistribuees"))
    adapter.activate()
    communicator.waitForShutdown()