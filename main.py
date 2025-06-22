import audio_pitch_extractor
import pitchMatching
import noteToEvent
import time
import threading
import queue
import json
import requests

import threading                           # To run sightreading in parallel
import time                                # For delays between notes
import audio_pitch_extractor              # Your custom pitch detection module
import pitchMatching                       # Your custom pitch rating logic
import noteToEvent         



ratings = []
musicFile = "simple_test_piece.musicxml"

bpm = 120
intendedNotes = noteToEvent.xmlToEvent(musicFile, bpm)

final_score = None  # new global variable
isDone = False  # new global variable


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
    final_score = totalRating # is this what the accuracy score is sergei
    isDone = True  # signal that sightreading is done

    # sightreading is done
  
if __name__ == "__main__":
    mainLoop()
