import audio_pitch_extractor
import pitchMatching
import noteToEvent
import time
import threading
import queue
import json
import requests

musicFile = "BeetAnGeSample.musicxml"
bpm = 120
intendedNotes = noteToEvent.xmlToEvent(musicFile, bpm)
