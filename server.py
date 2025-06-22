from flask import Flask, jsonify, request
import threading
import main
import time

app = Flask(__name__)

# Shared state for live updates
live_data = {
    'current_rating': 0,
    'current_note': None,
    'final_score': None,
    'done': False
}

# Thread target for mainLoop
def run_main_loop():
    numberOfNotes = 0
    totalRating = 0
    bpm = main.bpm
    intendedNotes = main.intendedNotes
    for note in intendedNotes:
        live_data['current_note'] = str(note)
        rating = main.pitchMatching.noteMatch(note)
        totalRating += rating
        numberOfNotes += 1
        live_data['current_rating'] = rating
        time.sleep(60.0 / bpm)
    totalAccuracy = totalRating / numberOfNotes if numberOfNotes else 0
    live_data['final_score'] = totalAccuracy
    live_data['done'] = True

@app.route('/start_practice', methods=['POST'])
def start_practice():
    # Reset state
    live_data['current_rating'] = 0
    live_data['current_note'] = None
    live_data['final_score'] = None
    live_data['done'] = False
    t = threading.Thread(target=run_main_loop)
    t.start()
    return jsonify({'status': 'started'})

@app.route('/live_rating', methods=['GET'])
def get_live_rating():
    return jsonify(live_data)

if __name__ == '__main__':
    app.run(debug=True)

