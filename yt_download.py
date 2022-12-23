from pytube import Playlist
import os

def download_video_as_mp3(url):
    playList = Playlist(url)

    # look through all video in the playlist
    for i,d in enumerate(playList.videos):
        print("d title",d.title)
        if d.title.encode('utf-8') not in fileName:
          print("Downloaded: ", i, " / ", len(playList.videos))
          download_file = d.streams.first().download(output_path=path)
          # get the the file
          base, _ = os.path.splitext(download_file)
          # rename to mp3
          new_file = base + '.wav'
          if not os.path.exists(new_file):
            os.rename(download_file, new_file)
        else:
          print("Already Downloaded: ", i, " / ", len(playList.videos))



# get now path
path = os.path.dirname(__file__)+'\\downloads'

# get all download files name
fileName = os.listdir(path)
fileName = [os.path.splitext(f)[0].encode('utf-8') for f in fileName]
# print(fileName)

url = 'https://www.youtube.com/playlist?list=PL3oW2tjiIxvTUfDOkivqSDxrxfQccwxsN'

download_video_as_mp3(url)
