import audio_pitch_extractor
import pitchMatching
import noteToEvent
import time
import threading
import queue
import json
import requests    

from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

app = Flask(__name__)
CORS(app, resources={r"/final_score": {"origins": "http://localhost:5173"}}, supports_credentials=True)



ratings = []
musicFile = "simple_test_piece.musicxml"

bpm = 120
intendedNotes = noteToEvent.xmlToEvent(musicFile, bpm)

final_score = None  # new global variable

def mainLoop():
    numberOfNotes = 0
    totalRating = 0

    for note in intendedNotes:
        print(note)

        # if pitch is not None:
        #     result = audio_pitch_extractor.freq_to_note(pitch)
        #     print(result)

        numberOfNotes += 1
        rating = pitchMatching.noteMatch(note)
        totalRating += rating

        time.sleep(60.0/bpm)
        # print("volume", audio_pitch_extractor.get_note_volume())
        print()
        
    totalAccuracy = totalRating / numberOfNotes
    print(f"Total accuracy: {totalAccuracy:.2f}%")
    
    global final_score
    final_score = totalAccuracy


    # sightreading is done
    # try:
    #     requests.post("http://localhost:5000/set_sightreading_done")
    # except Exception as e:
    #     print("Failed to notify server:", e)

@app.route('/final_score')
def get_final_score():
    if final_score is not None:
        print("this is running")
        return jsonify({'score': final_score})
    else:
        return jsonify({'error': 'Score not ready'}), 503

if __name__ == "__main__":
    # Run mainLoop in a background thread
    threading.Thread(target=mainLoop).start()
    
    # Start the Flask server
    # app.run(host="0.0.0.0", port=5000)
    app.run(debug=True, port=5000)
