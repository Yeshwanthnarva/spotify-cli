FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "spotify_cli.py"]
COPY requirements.txt /app/requirements.txt
# This Dockerfile sets up a Python environment for the Spotify CLI application.
# It installs the necessary dependencies from requirements.txt and runs the spotify_cli.py script.
# Ensure that the requirements.txt file is present in the same directory as this Dockerfile.