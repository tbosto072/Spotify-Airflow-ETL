import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError
import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_recent_tracks():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-recently-played",
        cache_path=os.path.join(os.path.dirname(__file__), ".cache")
    ))

    try: 
        results = sp.current_user_recently_played(limit=50)
        return results
    except SpotifyOauthError:
        print("Authorization failed: Check your credentials or re-authenticate.")
        return None
    except requests.exceptions.RequestException:
        print("Network error while contacting Spotify.")
        return None
    

