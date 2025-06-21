import time
import audio_pitch_extractor
chunk = 250  # length of time between measurements  in ms
incorrectPenalty = 20  # penalty for being out of tune
semitoneRounded = 5.94630943593


"""
pitch matching function
takes 2 pitches in hz, returns the % error * semitoneErrorMult if within a semitone
returns the % error * overSemitoneErrorMult if over a semitone, 
otherwise returns incorrectPenalty for errors greater than the pitchTolerance

"""
def pitchMatch(currentPitch, targetPitch):
    if targetPitch != 0:
        percentageError = (abs(currentPitch - targetPitch) / targetPitch) * 100  # percentage error relative to target pitch

        if percentageError < semitoneRounded / 2:  # within a 1/4 tone
          return 100
        elif percentageError < semitoneRounded * 2:
        # Scale from 100 to 0
          return 100 - percentageError*percentageError
        else:
            return 0  # more than a full tone off
    else:
        if currentPitch < 26 or currentPitch > 4186 or volumeExtractor.quietCheck():
            return 100  # if target pitch is 0, we assume the player is not playing a note


def noteMatch(intendedNote, playedNoteFunc):
    """
    Compares player's pitch with intended pitch every chunk ms
    - `intendedNote`: dict with 'time', 'duration', 'pitch'
    - `playedNoteFunc`: function returning current pitch
    returns rating integer 0-100
    """
    rating = 100
    startTime = intendedNote["time"]
    endTime = startTime + intendedNote["duration"]
    targetPitch = intendedNote["pitch"]
    currentTime = startTime

    while currentTime < endTime:
        currentPitch = audio_pitch_extractor.get_note_freq(0.075) # get the current pitch
        rating = max(pitchMatch(currentPitch, targetPitch), 0)  # prevent negative score
        time.sleep(chunk / 1000)  # wait chunk milliseconds
        currentTime += chunk

    return rating
