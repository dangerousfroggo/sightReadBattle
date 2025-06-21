import pyaudio
import time
import numpy as np
import math
from collections import Counter

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2048  # Larger chunk for better pitch accuracy

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def freq_to_note(freq):
    if freq <= 0:
        return None
    midi = int(round(69 + 12 * np.log2(freq / 440)))
    note_name = NOTE_NAMES[midi % 12]
    octave = midi // 12 - 1
    return f"{note_name}{octave}"

def autocorrelation_pitch(signal, fs):
    signal = signal - np.mean(signal)
    corr = np.correlate(signal, signal, mode='full')
    corr = corr[len(corr)//2:]
    d = np.diff(corr)
    start = np.where(d > 0)[0][0]
    peak = np.argmax(corr[start:]) + start
    if peak == 0:
        return 0
    return fs / peak

def main():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Listening... Press Ctrl+C to stop.")
    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio = np.frombuffer(data, dtype=np.int16).astype(np.float32)
            freq = autocorrelation_pitch(audio, RATE)
            note = freq_to_note(freq)
            if note:
                print(f"Detected note: {note} ({freq:.2f} Hz)      ", end='\r')
            else:
                print("No note detected.                ", end='\r')
    except KeyboardInterrupt:
        print("\nStopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()