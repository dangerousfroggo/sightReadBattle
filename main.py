import audio_pitch_extractor
import pitchMatching
import noteToEvent
import time
import threading
import queue
import json
import requests


ratings = []
musicFile = "BeetAnGeSample.musicxml"
bpm = 120
intendedNotes = noteToEvent.xmlToEvent(musicFile, bpm)
def mainLoop():
    for note in intendedNotes:
        print(note)
        pitch = audio_pitch_extractor.get_note_freq()
        print(pitch)

        # if pitch is not None:
        #     result = audio_pitch_extractor.freq_to_note(pitch)
        #     print(result)
        rating = pitchMatching.noteMatch(pitch, note["pitch"],10 )
        print(rating)
        time.sleep(60.0/bpm)

if __name__ == "__main__":
    mainLoop()
