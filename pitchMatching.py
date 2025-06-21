import time
import audio_pitch_extractor
import math
chunk = 250  # length of time between measurements  in ms
incorrectPenalty = 20  # penalty for being out of tune
semitoneRounded = 1.0594630943593


def freq_to_midi(freq):
    return 69 + 12 * math.log2(freq / 440)

"""
pitch matching function
takes 2 pitches in hz, returns the % error * semitoneErrorMult if within a semitone
returns the % error * overSemitoneErrorMult if over a semitone, 
otherwise returns incorrectPenalty for errors greater than the pitchTolerance

"""
def pitchMatch(expected_freq, played_freq, pitchTolerance):
    
    expected_midi = freq_to_midi(expected_freq)
    played_midi = freq_to_midi(played_freq)
    diff = abs(expected_midi - played_midi)

    if diff <= 0.25:  # within 1/4 semitone — nearly perfect
        return 100
    elif diff <= 0.5: # within 1/2 semitone
        # linear drop from 100 to 95 over 0.5 semitones
        return int(100 - diff * 10)  # drops to 95 at 0.5 semitones
    elif diff <= 1:  # within 1 semitone
        return int(95 - (diff - 0.5) * 90)  # drops to ~50 at 1 semitone
    elif diff <= 2:  # more than a semitone but less than a full tone
        return int(50 - (diff - 1) * 50)  # linear drop to 0
    else:
        return 0


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
        rating = max(pitchMatch(currentPitch, targetPitch, tolerance), 0)  # prevent negative score
        time.sleep(chunk / 1000)  # wait chunk milliseconds
        currentTime += chunk

    return rating

