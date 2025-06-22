import audio_pitch_extractor
import pitchMatching
import noteToEvent
import time
import threading
import queue
import json
import requests


ratings = []
musicFile = "simple_test_piece.musicxml"

bpm = 120
intendedNotes = noteToEvent.xmlToEvent(musicFile, bpm)

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

    # sightreading is done
    try:
        requests.post("http://localhost:5000/set_sightreading_done")
    except Exception as e:
        print("Failed to notify server:", e)

if __name__ == "__main__":
    mainLoop()
