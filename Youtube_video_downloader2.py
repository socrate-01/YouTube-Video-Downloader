from pytube import YouTube
from sys import argv
print("Welcome to socratis youtube downloader!")
print("""                                  __
  __________   ________________ _/  |_  ____
 /  ___/  _ \_/ ___\_  __ \__  \\   __\/ __ \
 \___ (  <_> )  \___|  | \// __ \|  | \  ___/
/____  >____/ \___  >__|  (____  /__|  \___  >
     \/           \/           \/          \/ """)
link = input("Paste the video's link you want to donlad please : ")
link = str(link)
yt = YouTube(link)
print("Title : ",yt.title)
print("View : ",yt.views)
yd = yt.streams.get_highest_resolution()
yd.download("/home/downloads/YoutubeDownload")
