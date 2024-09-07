# spotify-local-file-links-generator
Very simple script that generates Spotify local file links, for adding to a playlist in order.

# Why?
When searching for an album imported to Spotify through local files, the songs are almost always in a different order from the tracklist, which requires manual reordering when adding it to a playlist.

![Screenshot_20240907_115142](https://github.com/user-attachments/assets/047e3086-ee36-4bb0-b372-42a29c889b95)
![Screenshot_20240907_115153](https://github.com/user-attachments/assets/46b28d3b-4e82-466b-b7e9-3da2ccca03e9)

The process can get tedious when adding an album with more than 30 tracks, so the script aims to automate this and generate a list of links for the audio files in the current folder, sorted by file name, which can then be pasted to the Spotify window while looking at a playlist.

![Screenshot_20240907_115513](https://github.com/user-attachments/assets/5551df98-8ed3-4088-bec1-a8b96f806eca)

# Requirements
- Python
- pip
- TinyTag (can be installed through pip)
