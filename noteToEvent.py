from music21 import *
def xmlToEvent(xmlFile, bpm = 60):
    score = converter.parse(xmlFile) #lowkey no idea what tf a converter is but basically this parses it 
    events = []
    flat_score = score.parts[0].flat.notesAndRests #flattens score to series of notes and rests
    msPerBeat = 60000/bpm
    print(flat_score)
    for n in flat_score:
        if isinstance(n, note.Note):
            pitch = n.pitch.frequency
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