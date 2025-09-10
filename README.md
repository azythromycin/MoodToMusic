# MoodToMusic

A web application that analyzes user input to determine mood and provides corresponding Spotify playlists.

## Overview

MoodToMusic uses AI-powered mood analysis to match user descriptions with appropriate music playlists. Users describe their current feelings or situation, and the application returns a curated Spotify playlist that matches their emotional state.

## Features

- Natural language mood analysis using Ollama AI
- Spotify playlist integration
- Simple web interface for user input
- Automatic mood categorization (happy, sad, angry, tired, agitated, excited, depressed, stressed, motivated)

## Technology Stack

- **Backend**: Python Flask
- **AI Model**: Ollama with Llama3
- **Music API**: Spotify Web API
- **Frontend**: HTML, CSS
- **Authentication**: Spotify Client Credentials

## Installation

### Prerequisites

- Python 3.7+
- Spotify Developer Account
- Ollama installed locally

### Setup

1. Install Python dependencies:
   ```bash
   pip install flask spotipy ollama
   ```

2. Install Ollama and pull the Llama3 model:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ollama pull llama3
   ```

3. Configure Spotify credentials:
   - Create a Spotify app in the Spotify Developer Dashboard
   - Update `client_id` and `client_secret` in `app.py`

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:9092`

## Usage

1. Enter a description of your current mood or situation in the text input
2. Click "Explore!" to analyze your mood
3. The application will return a Spotify playlist embedded in the page

## Project Structure

```
MoodToMusic/
├── app.py          # Flask application with mood analysis and Spotify integration
├── index.html      # Main user interface
├── style.css       # Styling for the web interface
├── bgpic.png       # Background image
└── README.md       # This file
```

## API Endpoints

- `GET /explore` - Analyzes user mood and returns Spotify playlist
  - Parameters: `mood` (text input), `SubmitButton` (form submission)

## Dependencies

- Flask - Web framework
- Spotipy - Spotify Web API client
- Ollama - Local AI model interface

## Configuration

The application requires Spotify API credentials to function. Update the following variables in `app.py`:

```python
client_id = 'your_spotify_client_id'
client_secret = 'your_spotify_client_secret'
```

## Limitations

- Requires active internet connection for Spotify API calls
- Ollama must be running locally for mood analysis
- Limited to predefined mood categories
- Spotify playlists are limited to search results

## License

This project is for educational and personal use.
