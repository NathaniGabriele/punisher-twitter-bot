import json
import lyricsgenius
import random
import os

GENIUS_CLIENT_ID = os.environ['GENIUS_CLIENT_ID']
GENIUS_SECRET = os.environ['GENIUS_SECRET']
TOKEN = os.environ['TOKEN']

genius = lyricsgenius.Genius(TOKEN)

# album = genius.search_album("Punisher", "Phoebe Bridgers")
# album.save_lyrics()

file = open("Lyrics_Punisher.json")
data = json.load(file)  # convert json into dict

tracks = data["tracks"]  # list with all the tracks

# Finding the lyrics in the dictionary data
lyrics_list = []
for track in tracks:
    lyrics = track["song"]["lyrics"]
    lyrics_list.append(lyrics.strip("\u2005"))

# Dividing the list through "\n"
clean_list = []
for string in lyrics_list:
    sentence = string.split("\n")
    clean_list.append(sentence)

# Transforming a list of list into a flat list
final_list = []
for sublist in clean_list:
    for item in sublist:
        final_list.append(item)

# Cleaning values from the list
for elem in list(final_list):
    exclude_values = ['', '[Chorus]', '[Outro]', '[Refrain]', '[Verse 1]', '[Verse 2]', '[Verse 3]', '[Verse 4]']
    if elem in exclude_values:
        final_list.remove(elem)


tweet_lyric = random.choice(final_list)

