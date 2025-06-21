import time
import audio_pitch_extractor
chunk = 250  # length of time between measurements  in ms
incorrectPenalty = 20  # penalty for being out of tune
ratings = []

def pitchMatch(pitch1, pitch2, pitchTolerance):
    """
    Returns pitch error if within tolerance, otherwise returns incorrectPenalty
    """
    diff = abs(pitch1 - pitch2)
    return diff if diff < pitchTolerance else incorrectPenalty

def noteMatch(intendedNote, playedNoteFunc, tolerance):
    """
    Compares player's pitch with intended pitch every chunk ms
    - `intendedNote`: dict with 'time', 'duration', 'pitch'
    - `playedNoteFunc`: function returning current pitch
    - `tolerance`: pitch tolerance
    returns rating integer 0-100
    """
    rating = 100
    startTime = intendedNote["time"]
    endTime = startTime + intendedNote["duration"]
    targetPitch = intendedNote["pitch"]
    currentTime = startTime

    while currentTime < endTime:
        currentPitch = audio_pitch_extractor.get_note_freq(0.075) # get the current pitch
        penalty = pitchMatch(currentPitch, targetPitch, tolerance)
        rating -= penalty
        rating = max(rating, 0)  # prevent negative score
        time.sleep(chunk / 1000)  # wait chunk milliseconds
        currentTime += chunk

    return rating

