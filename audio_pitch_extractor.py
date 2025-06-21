import sounddevice as sd
import numpy as np
from scipy.fft import rfft, rfftfreq
import time

FS = 44100
FRAME_DURATION = 0.1
BUFFER_SIZE = int(FS * FRAME_DURATION)

def extract_pitch(audio, fs):
    N = len(audio)
    window = np.hanning(N)
    audio = audio * window
    yf = np.abs(rfft(audio))
    xf = rfftfreq(N, 1 / fs)
    idx = np.argmax(yf)
    freq = xf[idx]
    return freq

def audio_callback(indata, frames, time_info, status):
    start_time = time.time()
    
    if status:
        print("Stream status:", status)
    
    audio = indata[:, 0]
    pitch = extract_pitch(audio, FS)
    
    elapsed = time.time() - start_time
    print(f"Pitch: {pitch:.2f} Hz | Processing Time: {elapsed:.4f} s")
    
    return pitch


with sd.InputStream(callback=audio_callback, channels=1, samplerate=FS,
                    blocksize=BUFFER_SIZE, dtype='float32'):
    print("Listening... (press Ctrl+C   to stop)")
    sd.sleep(5000)  # Run for 5 seconds (about 50 frames)
