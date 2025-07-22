from flask import Flask, request, jsonify, render_template
from ollama import chat
from ollama import ChatResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

#Spotify credentials
client_id = '32fe4162141f409a8d6dd1aefe590b36'
client_secret = '67587933517347969fd0b4c5118d128e'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

#Creating spotify client
sp = spotipy.Spotify(auth_manager=auth_manager)

#Waitress
@app.route('/explore', methods=['GET'])
def login():
    mood = request.args.get('mood')
    buttonValue = request.args.get('SubmitButton')

    rawUserInput = mood

    promptUsingUserInputText = f'Here is a paragraph(s) inputted by a user: {rawUserInput}. After carefully analyzing the tone and user\'s way of speaking, determine and describe their mood in ONE WORD. JUST ONE WORD AND CATEGORIZE THEIR MOOD ACCORDING TO ANY OF THESE MOODS: HAPPY, SAD, ANGRY, TIRED, AGITATED, EXCITED, DEPRESSED, STRESSED, MOTIVATED... NOTHING ELSE. DON\'T RESPOND WITH AN ENTIRE SENTENCE. JUST CONCLUDE USER\'S INPUT IN ONE WORD... WHICH WOULD BE THE MOOD BUT ANSWER WITH ONLY ONE SIMPLE WORD'

    response: ChatResponse = chat(model='llama3', messages=[
        {
        'role': 'user', 'content': promptUsingUserInputText}
    ])

    finalOneWordResponse = response['message']['content'].strip()

    # Search for playlists matching a mood. Limit our results to only 1 result and capture the first result that pops up when entered user's mood
    results = sp.search(q=finalOneWordResponse, type='playlist', limit=1)
    playlist_url = results['playlists']['items'][0]['external_urls']['spotify'] 
    #To obtain the playlist ID, we split the url with respect to / and only take the last of the split terms
    playlist_id = playlist_url.split("/")[-1]
    #Embedding spotify web player now using the right format
    return render_template("embedpage.html", embed_url=f"https://open.spotify.com/embed/playlist/{playlist_id}")
    

    
