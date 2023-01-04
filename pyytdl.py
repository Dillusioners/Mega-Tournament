#importing package pytube
from pytube import YouTube

#taking input

url = input("Paste the url of the video you desire: ")
u1 = YouTube(url)
while url == "":
    url = input("Paste the url correctly!!!")
    u1 = YouTube(url)
#printing url and thumbnail
print("Video Title: ", u1.title)
print("Video Thumbnail Link: ", u1.thumbnail_url)
print("Fetching stream details....")
print("Almost there....")
stream = u1.streams.all()
vid = list(enumerate(stream))
for i in vid:
    print(i)
#downloading video
index = int(input("Enter the index of the stream choice"))
stream[index].download()

print("Video installed successfully: ")
