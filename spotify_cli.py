import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os
import base64
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Load environment variables
if not load_dotenv():
    print("Warning: .env file not found or could not be loaded.")

# Fetch credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")

# Validate credentials
if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET or not SPOTIFY_REDIRECT_URI or not GENIUS_API_KEY:
    print("Error: Missing environment variables. Please check your .env file.")
    exit()

# Initialize Spotify OAuth
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=SPOTIFY_REDIRECT_URI,
                        scope="user-read-currently-playing user-top-read")

# Retrieve or refresh access token
try:
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f"Authorize the app by visiting this URL: {auth_url}")
        auth_code = input("Enter the redirected URL: ").strip()
        token_info = sp_oauth.get_access_token(auth_code.split("code=")[-1])

    access_token = token_info['access_token']
    print("New Token:", access_token)
except Exception as e:
    print(f"Error retrieving access token: {e}")
    exit()

# Create an authenticated Spotify client
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Function to get currently playing track
def get_currently_playing():
    try:
        track = sp.current_user_playing_track()
        if track and track['item']:
            song_name = track['item']['name']
            artist_name = track['item']['artists'][0]['name']
            print(f"🎵 Currently playing: {song_name} by {artist_name}")
            return song_name, artist_name
        else:
            print("No track currently playing.")
            return None, None
    except Exception as e:
        print(f"Error fetching currently playing track: {e}")
        return None, None

# Function to fetch user's top artists
def get_user_top_artists():
    try:
        top_artists = sp.current_user_top_artists(limit=5)
        seed_artists = [artist['id'] for artist in top_artists['items']]
        return seed_artists
    except Exception as e:
        print(f"Error fetching top artists: {e}")
        return []

# Function to get song recommendations
def get_recommendations():
    try:
        seed_artists = get_user_top_artists()
        if not seed_artists:
            print("No top artists found. Defaulting to popular genres.")
            results = sp.recommendations(seed_genres=["pop", "rock"], limit=5)
        else:
            results = sp.recommendations(seed_artists=seed_artists, limit=5)

        print("🎶 Recommended Tracks:")
        for idx, track in enumerate(results['tracks']):
            print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")
    except Exception as e:
        print(f"Error fetching recommendations: {e}")

# Function to search song lyrics on Genius
def search_song_on_genius(song_name, artist_name):
    base_url = "https://api.genius.com/search"
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    params = {"q": f"{song_name} {artist_name}"}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        json_data = response.json()
        
        if json_data["response"]["hits"]:
            song_url = json_data["response"]["hits"][0]["result"]["url"]
            return song_url
        else:
            return "Lyrics not found."
    except Exception as e:
        return f"Error fetching lyrics: {e}"

# Function to get lyrics
def get_lyrics():
    song_name, artist_name = get_currently_playing()
    if song_name and artist_name:
        song_url = search_song_on_genius(song_name, artist_name)
        print(f"🎤 Lyrics available here: {song_url}")
    else:
        print("No track currently playing.")

# Command-line interaction
command = input("Enter command (current, lyrics, recommendations): ").strip().lower()

if command == "current":
    get_currently_playing()
elif command == "lyrics":
    get_lyrics()
elif command == "recommendations":
    get_recommendations()
else:
    print("Invalid command. Use 'current', 'lyrics', or 'recommendations'.")
# End of the Spotify CLI script
