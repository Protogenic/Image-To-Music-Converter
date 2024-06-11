import mido
from mido import Message, MidiFile, MidiTrack


def majorChord(key, duration, track):
    track.append(Message('note_on', channel=0, note=key, velocity=64, time=0))
    track.append(Message('note_on', channel=0, note=key + 4, velocity=64, time=0))
    track.append(Message('note_on', channel=0, note=key + 7, velocity=64, time=0))
    track.append(Message('note_off', channel=0, note=key, velocity=64, time=duration))
    track.append(Message('note_off', channel=0, note=key + 4, velocity=64, time=0))
    track.append(Message('note_off', channel=0, note=key + 7, velocity=64, time=0))


def minorChord(key, duration, track):
    track.append(Message('note_on', channel=0, note=key, velocity=64, time=0))
    track.append(Message('note_on', channel=0, note=key + 3, velocity=64, time=0))
    track.append(Message('note_on', channel=0, note=key + 7, velocity=64, time=0))
    track.append(Message('note_off', channel=0, note=key, velocity=64, time=duration))
    track.append(Message('note_off', channel=0, note=key + 3, velocity=64, time=0))
    track.append(Message('note_off', channel=0, note=key + 7, velocity=64, time=0))