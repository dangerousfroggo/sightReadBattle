import time

chunk = 50  # length of time between measurements  in ms
incorrectPenalty = 20  # penalty for being out of tune
ratings = []

def pitchMatch(pitch1, pitch2, pitchTolerance):
    """
    Returns pitch error if within tolerance, otherwise returns fixed penalty
    """
    diff = abs(pitch1 - pitch2)
    return diff if diff < pitchTolerance else incorrectPenalty

def noteMatch(intendedNote, playedNoteFunc, tolerance):
    """
    Compares the player's pitch to the intended pitch over time
    - `intendedNote`: dict with 'time', 'duration', 'pitch'
    - `playedNoteFunc`: function returning current pitch
    - `tolerance`: pitch tolerance
    """
    rating = 100
    startTime = intendedNote["time"]
    endTime = startTime + intendedNote["duration"]
    targetPitch = intendedNote["pitch"]
    currentTime = startTime

    while currentTime < endTime:
        currentPitch = playedNoteFunc()  # get the current pitch
        penalty = pitchMatch(currentPitch, targetPitch, tolerance)
        rating -= penalty
        rating = max(rating, 0)  # prevent negative score
        time.sleep(chunk / 1000)  # wait chunk milliseconds
        currentTime += chunk

    return rating

