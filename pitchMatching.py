import time
import audio_pitch_extractor
chunk = 250  # length of time between measurements  in ms
incorrectPenalty = 20  # penalty for being out of tune
semitoneRounded = 1.0594630943593


"""
pitch matching function
takes 2 pitches in hz, returns the % error * semitoneErrorMult if within a semitone
returns the % error * overSemitoneErrorMult if over a semitone, 
otherwise returns incorrectPenalty for errors greater than the pitchTolerance

"""
def pitchMatch(pitch1, pitch2, pitchTolerance):
    
    # if within a semitone, calculate the error percentage
    # if within a full note, return the incorrect penalty
    # if more than a full note off, return 0


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

