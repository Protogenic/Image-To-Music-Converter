import mido
from mido import Message, MidiTrack
from image_to_music.music_settings import SIXTEENTH_NOTE, EIGHTH_NOTE, QUARTER_NOTE


def create_drums(tempo):
    if tempo < 100:
        tracks = create_classic_drums(tempo)
    elif 100 <= tempo <= 160:
        tracks = create_eighth_drums(tempo)
    else:
        tracks = create_punk_drums(tempo)

    return tracks


def create_punk_drums(tempo):
    tracks = []

    bass_drum = MidiTrack()
    snare_drum = MidiTrack()
    cymbals = MidiTrack()

    bass_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    bass_drum.append(Message('control_change', control=7, value=120, time=0))
    snare_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    cymbals.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(32):
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=SIXTEENTH_NOTE * 8, channel=9))
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=SIXTEENTH_NOTE * 2, channel=9))
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=SIXTEENTH_NOTE * 6, channel=9))

    for _ in range(64):
        snare_drum.append(Message('note_off', note=38, velocity=100, time=SIXTEENTH_NOTE * 4, channel=9))
        snare_drum.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
        snare_drum.append(Message('note_off', note=38, velocity=100, time=SIXTEENTH_NOTE * 4, channel=9))

    for _ in range(32):
        cymbals.append(Message('note_on', note=49, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=49, velocity=100, time=QUARTER_NOTE, channel=9))
        for _ in range(3):
            cymbals.append(Message('note_on', note=46, velocity=100, time=0, channel=9))
            cymbals.append(Message('note_off', note=46, velocity=100, time=QUARTER_NOTE, channel=9))

    tracks.append(bass_drum)
    tracks.append(snare_drum)
    tracks.append(cymbals)

    return tracks


def create_eighth_drums(tempo):
    tracks = []

    bass_drum = MidiTrack()
    snare_drum = MidiTrack()
    cymbals = MidiTrack()

    bass_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    bass_drum.append(Message('control_change', control=7, value=120, time=0))
    snare_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    cymbals.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(64):
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=QUARTER_NOTE * 2, channel=9))

    for _ in range(64):
        snare_drum.append(Message('note_off', note=38, velocity=100, time=EIGHTH_NOTE * 2, channel=9))
        snare_drum.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
        snare_drum.append(Message('note_off', note=38, velocity=100, time=EIGHTH_NOTE * 2, channel=9))

    for _ in range(64):
        for _ in range(3):
            cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
            cymbals.append(Message('note_off', note=42, velocity=100, time=SIXTEENTH_NOTE, channel=9))

        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=EIGHTH_NOTE, channel=9))

        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        for _ in range(3):
            cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
            cymbals.append(Message('note_off', note=42, velocity=100, time=SIXTEENTH_NOTE, channel=9))

    tracks.append(bass_drum)
    tracks.append(snare_drum)
    tracks.append(cymbals)

    return tracks


def create_classic_drums(tempo):
    tracks = []

    bass_drum = MidiTrack()
    snare_drum = MidiTrack()
    cymbals = MidiTrack()

    bass_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    bass_drum.append(Message('control_change', control=7, value=120, time=0))
    snare_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    cymbals.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(16):
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=QUARTER_NOTE * 5, channel=9))
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=QUARTER_NOTE * 3, channel=9))

    for _ in range(32):
        snare_drum.append(Message('note_off', note=38, velocity=100, time=QUARTER_NOTE * 2, channel=9))
        snare_drum.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
        snare_drum.append(Message('note_off', note=38, velocity=100, time=QUARTER_NOTE * 2, channel=9))

    for _ in range(16):
        cymbals.append(Message('note_on', note=46, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=46, velocity=100, time=EIGHTH_NOTE, channel=9))
        for _ in range(15):
            cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
            cymbals.append(Message('note_off', note=42, velocity=100, time=EIGHTH_NOTE, channel=9))

    tracks.append(bass_drum)
    tracks.append(snare_drum)
    tracks.append(cymbals)

    return tracks
