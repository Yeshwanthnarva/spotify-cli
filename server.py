from flask import Flask, request, redirect
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Spotify API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:27228/spotify_callback"

# Set up Spotify authentication
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope="user-read-currently-playing")

@app.route("/")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/spotify_callback")
def spotify_callback():
    code = request.args.get("code")
    if not code:
        return "Error: No authorization code received."
    
    token_info = sp_oauth.get_access_token(code)
    return f"Access Token: {token_info['access_token']}"

if __name__ == "__main__":
    app.run(port=27228)
