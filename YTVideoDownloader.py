# Kenneth Otis
# Youtube Video Downloader
from pytube import YouTube
from pytube import exceptions
import time

# getting the link from the user
link=input("Please enter the link of the YouTube Video you would like to download: ")
yt=YouTube(link)

# showing the video's details
print("Title: ", yt.title)
time.sleep(1)
print ("Views: ", yt.views)
time.sleep(1)
print("Length of video: ", yt.length)
time.sleep(1)
print ("Rating of the video: ", yt.rating)
time.sleep(1)

# Get the highest resolution
stream= yt.streams.first()

#Starting download 
print ("\nDownloading to Desktop...")
stream.download('Desktop')
time.sleep(1)
print("\nDownload complete!\n")