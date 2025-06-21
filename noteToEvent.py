from music21 import *
def xmlToEvent(xmlFile, bpm = 60):
    """
    Converts a music21 stream (parsed from an xml file) into a list of events
    suitable for use in pitchMatching.py. Each event is a dictionary with
    the following keys:

    - time: the time, in milliseconds, at which the event starts
    - duration: the length, in milliseconds, of the event
    - pitch: the frequency of the note (0 if the event is a rest)

    :param xmlFile: the path to an xml file containing a music21 stream
    :param bpm: the tempo of the piece, in beats per minute
    :return: a list of events
    """
    score = converter.parse(xmlFile) #lowkey no idea what tf a converter is but basically this parses it 
    events = []
    flat_score = score.parts[0].flat.notesAndRests #flattens score to series of notes and rests
    msPerBeat = 60000/bpm
    print(flat_score)
    for n in flat_score:
        if isinstance(n, note.Note):
            pitch = round(n.pitch.frequency, 2) #rounding to 2 decimal places for comparisonn.pitch.frequency
        elif isinstance(n,note.Rest):
            pitch = 0
        elif isinstance(n,note.Chord):
            pitch = n[0].pitch.frequency
        else:
            continue #skip if code is neither (bad way of dealing with erraneous input, fix later to identify dynamics markings etc )
        event = {
            "time": n.offset*msPerBeat,
            "duration": n.duration.quarterLength*msPerBeat,
            "pitch": pitch
        }
        events.append(event)
    return events