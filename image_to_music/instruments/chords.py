import mido
from mido import Message, MidiTrack
from image_to_music.music_settings import QUARTER_NOTE


def create_chords_track(hsv_array, avg_hue, tempo):
    track = MidiTrack()
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    track.append(Message('program_change', program=30, channel=0))
    track.append(Message('control_change', control=7, value=50, time=0))

    if 0 <= avg_hue < 86 or 215 <= avg_hue <= 255:
        tone = 'major'
    else:
        tone = 'minor'

    for _ in range(2):
        for row in hsv_array:
            for pixel in row:
                hue, sat, val = pixel
                sat = 50 + round(sat / 10)

                for _ in range(4):
                    create_quint_chord(sat, tone, track)

    return track


def create_quint_chord(key, tone, track):
    key_change = 0
    if tone == 'major':
        key_change = 4
    elif tone == 'minor':
        key_change = 3

    track.append(Message('note_on', channel=0, note=key, velocity=64, time=0))
    track.append(Message('note_on', channel=0, note=key + key_change, velocity=64, time=0))
    track.append(Message('note_on', channel=0, note=key + 7, velocity=64, time=0))
    track.append(Message('note_off', channel=0, note=key, velocity=64, time=QUARTER_NOTE))
    track.append(Message('note_off', channel=0, note=key + key_change, velocity=64, time=0))
    track.append(Message('note_off', channel=0, note=key + 7, velocity=64, time=0))

    return track
