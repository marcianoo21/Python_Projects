import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Creating spotify playlist top 100 songs from provided year



USER_NAME = "USER_NAME"
SPOT_ENDOPOINT = f"https://api.spotify.com/v1/users/{USER_NAME}/playlists"
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
PLAYLIST_ID = ""
year_travel = input("Which year do you want to travel to? Type the year in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year_travel}"

billboard_web = requests.get(URL)
bill_webpage = billboard_web.text

soup = BeautifulSoup(bill_webpage, "html.parser")

all_songs = soup.select("li ul li h3") 

songs_titles = [song.getText().strip() for song in all_songs]
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USER_NAME, 
    )
)

spotify_uris = []
year = year_travel.split("-")[0]
user_id = sp.current_user()["id"]
song_uris = []
year = year.split("-")[0]
for song in songs_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Top 100 Songs", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)