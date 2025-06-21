import sounddevice as sd
import numpy as np
from scipy.fft import rfft, rfftfreq
import time
import mido

FRAME_DURATION = 0.2  # seconds (analyze every 0.2s)
FS = 44100    # sample rate

def record_audio(duration, fs):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    return audio.flatten()

def extract_pitch(audio, fs):
    N = len(audio)
    yf = np.abs(rfft(audio))
    xf = rfftfreq(N, 1 / fs)
    idx = np.argmax(yf)
    freq = xf[idx]
    return freq

def freq_to_midi_note(freq):
    if freq <= 0:
        return None
    midi_note = x
    return midi_note

def main():
    print("Press Ctrl+C to stop.")
    try:
        while True:
            audio = record_audio(FRAME_DURATION, FS)
            freq = extract_pitch(audio, FS)
            midi_note = freq_to_midi_note(freq)
            if midi_note is not None:
                print(f"Dominant frequency: {freq:.2f} Hz, MIDI note: {midi_note}")
            else:
                print(f"Dominant frequency: {freq:.2f} Hz, MIDI note: N/A")
            time.sleep(0.1)  # Wait for the rest of the 5 seconds
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
