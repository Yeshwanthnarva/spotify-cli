import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables
if not load_dotenv():
    print("Warning: .env file not found or could not be loaded.")

# Fetch credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Validate credentials
if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET or not SPOTIFY_REDIRECT_URI:
    print("Error: Missing environment variables. Please check your .env file.")
    exit()

# Encode client credentials for authentication
auth_str = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Set up headers for authentication
headers = {
    "Authorization": f"Basic {b64_auth_str}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Initialize Spotify OAuth (for user authentication)
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=SPOTIFY_REDIRECT_URI,
                        scope="user-read-currently-playing")

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

# Create an authenticated Spotify client (user authentication)
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Alternative client authentication (if only fetching public data)
sp_client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                                 client_secret=SPOTIFY_CLIENT_SECRET))

# Function to get currently playing track
def get_currently_playing():
    try:
        track = sp.current_user_playing_track()
        if track and track['item']:
            song_name = track['item']['name']
            artist_name = track['item']['artists'][0]['name']
            print(f"Currently playing: {song_name} by {artist_name}")
        else:
            print("No track currently playing. Make sure Spotify is open and playing.")
    except Exception as e:
        print(f"Error fetching currently playing track: {e}")

# Command-line usage
command = input("Enter command (current): ").strip().lower()
if command == "current":
    get_currently_playing()
else:
    print("Invalid command. Use 'current' to check playback.")
# Note: Ensure that the Spotify app is running and playing a track for the 'current' command to work.
# This script allows you to authenticate with Spotify and fetch the currently playing track.