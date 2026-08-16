# Purpose: Import Spotipy API library and OAuth for token generation. This will request the client ID and client secret of the app as well as the
# redirect URI to know where to open up the browser. It will prompt the user to allow the app to access their Spotify data like listening history, 
# and then it will generate an access token that's valid for one hour. This access token allows the app to have access to their data 
# without needing their password. This token gets sent with each API request to prove that you're allowed in, but it expires quickly.
# There's also a refresh token that's generated from OAuth. The refresh token allows your code to silently get a new access token 
# without having to reapprove access for the app every hour. OAuth handles this refresh automatically when you call current_user_recently_played().

import spotipy
import os 
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-recently-played"
    ))

results = sp.current_user_recently_played(limit=15) # Grabs 15 most recently streamed songs and returns JSON output

print(results.keys()) # Relevant key: 'items', results stores a list of play event items
print(results['items'][0].keys()) # Relevant keys: 'track' and 'played_at', each play event has track data and datetime data 
print(results['items'][0]['track'].keys()) # Relevant keys: 'album', 'artists', 'name': each track within a play event has this specific data

