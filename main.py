import scrapetube
import sys

path = input("filename: ")
channel_id = input("channel_id: ")
sys.stdout = open(path, 'w')

videos = scrapetube.get_channel(channel_id)

print(videos)

for video in videos:
    print("- [ ] ["+str(video['title']['runs'][0]['text'])+"](https://www.youtube.com/watch?v="+str(video['videoId'])+")")
