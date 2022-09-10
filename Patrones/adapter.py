"""
Patron de diseño: Adapter con PYTHON
Adapta 2 o más clases que no son polimórficas 
y las "une" en una clase.


"""
class AudioPlayer(object):
   def play(self, audioType, fileName):  

      #inbuilt support to play mp3 music files
      if(audioType=="mp3"):
         print("Playing mp3 file. Name: " + fileName + "\n\r")
      
      #mediaAdapter is providing support to play other file formats
      elif(audioType=="vlc" or audioType=="mp4"):
         self.mediaAdapter = MediaAdapter(audioType)
         self.mediaAdapter.play(audioType, fileName)
      
      else:
         print("Invalid media. " + audioType + " format not supported")
      

class MediaAdapter(object) :
   def __init__(self,audioType):
   
      if(audioType == "vlc" ):
         self.advancedMusicPlayer = VlcPlayer() 
      elif (audioType == "mp4"):
         self.advancedMusicPlayer = Mp4Player()
      
   def play(self, audioType, fileName):

      if(audioType == "vlc"):
         self.advancedMusicPlayer.playVlc(fileName)
      elif(audioType == "mp4" ):
         self.advancedMusicPlayer.playMp4(fileName)


class VlcPlayer(object):
   def playVlc(self, fileName):
      print("Playing VLC file")

   def playMp4(self, fileName):
      pass


class Mp4Player(object):
   def playVlc(self, fileName):
      pass

   def playMp4(self, fileName):
      print("Playing MP4 file")


audioPlayer = AudioPlayer()

audioPlayer.play("mp3", "beyond the horizon.mp3")
audioPlayer.play("mp4", "alone.mp4")
audioPlayer.play("vlc", "far far away.vlc")
audioPlayer.play("avi", "mind me.avi")
