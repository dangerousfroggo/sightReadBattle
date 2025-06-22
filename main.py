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
    for note in intendedNotes:
        print(note)

        # if pitch is not None:
        #     result = audio_pitch_extractor.freq_to_note(pitch)
        #     print(result)

        rating = pitchMatching.noteMatch(note)

        time.sleep(60.0/bpm)
        # print("volume", audio_pitch_extractor.get_note_volume())
        print()
        

if __name__ == "__main__":
    mainLoop()
