from tinytag import TinyTag
import urllib.parse
from os import listdir
from os.path import isfile, join

exts = [".mp3", ".flac", ".wav", ".m4a", ".ogg", ".opus"]

# Creates list of files in current path "." sorted by name
files = sorted(f for f in listdir(".") if isfile(join(".", f)))

# Creates file for writing list of links
f = open("links.txt", "w")

for i in files:
    # Only reads files with matching extensions from exts list
    if any(s in i for s in exts):
        tag = TinyTag.get(i)
        url = urllib.parse.quote

        artist = url(tag.artist)
        album = url(tag.album)
        title = url(tag.title)
        length = tag.duration
        
        f.write(f"https://open.spotify.com/local/{artist}/{album}/{title}/{int(length)}\n")