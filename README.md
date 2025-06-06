# 🎵 **Spotify CLI Tool**  
A lightweight command-line tool for **fetching currently playing tracks, lyrics, and recommendations** using the Spotify API. Works **for free Spotify accounts**! 🎶  

---

## 🚀 **Features**  
✅ Display **currently playing track** with details (artist, album, duration)  
✅ Fetch **song lyrics** using Lyrics.ovh API  
✅ Provide **music recommendations** based on track ID  
✅ **Dockerized** for easy deployment  
✅ Works on **Windows, Mac, and Linux**  

---

## 🛠 **Installation**  
### 1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Yeshwanthnarva/spotify-cli.git
cd spotify-cli

2️⃣ Install dependencies
bash
pip install -r requirements.txt

3️⃣ Set up your .env file with Spotify API keys
Create a .env file in the project folder and add:

plaintext
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:27228/spotify_callback

🔧 Usage
Run the CLI tool:

bash
python spotify_cli.py

Use the following commands inside the tool: 🔹 current → Show currently playing track 🔹 lyrics → Fetch song lyrics 🔹 recommend → Suggest similar tracks

📌 Docker Setup
1️⃣ Build the image
bash
docker build -t spotify-cli .

2️⃣ Run the container
bash
docker run -it --env-file .env spotify-cli

📸 Screenshots
🎵 Currently Playing	📜 Lyrics	🎧 Recommendations

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributions & Feedback
Feel free to fork the repo, submit pull requests, or open issues for improvements. If you find this project useful, ⭐ star the repo to support development! 🚀

📌 Next Features & Enhancements
🔹 Add album artwork preview in terminal 🔹 Improve lyrics fetching with multiple sources 🔹 Deploy to Google Cloud or AWS

