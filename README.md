# CLI-Based-Spotify-Controller

# 🎵 Spotify CLI Tool  
A command-line tool for fetching currently playing tracks, lyrics, and recommendations using Spotify API.

## 🚀 Features  
✅ Fetch currently playing track  
✅ Display song details (artist, album, duration)  
✅ Retrieve lyrics using Lyrics.ovh API  
✅ Provide music recommendations based on track ID  
✅ Dockerized for easy deployment  

## 🛠 Installation  

1️⃣ Clone the repository  
```bash
git clone https://github.com/Yeshwanthnarva/spotify-cli.git
cd spotify-cli

2️⃣ Install dependencies

bash
pip install -r requirements.txt

3️⃣ Set up your .env file with your Spotify API keys.

🔧 Usage
Run the CLI tool:

bash
python spotify_cli.py

Use the following commands inside the tool:

current → Show currently playing track

lyrics → Fetch lyrics

recommend → Suggest similar tracks

📌 Docker Setup

1️⃣ Build the image

bash
docker build -t spotify-cli .

2️⃣ Run the container

bash
docker run -it --env-file .env spotify-cli