import mido
from mido import Message, MidiTrack
from image_to_music.music_settings import EIGHTH_NOTE, SCALES


def create_solo(tempo, hsv_array, hue):
    scale = pick_scale(hue)

    track = MidiTrack()
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    track.append(Message('program_change', program=29, channel=0))
    track.append(Message('control_change', control=7, value=120, time=0))

    empty_border = 20
    for row in hsv_array:
        for pixel in row:
            value = pixel[0]
            if value < empty_border:
                track.append(Message('note_off', channel=0, note=0, velocity=64, time=EIGHTH_NOTE))
            else:
                index = int(((value - empty_border) / (255 - empty_border)) * (len(scale) - 1))
                note = scale[index]
                track.append(Message('note_on', channel=0, note=note, velocity=64, time=0))
                track.append(Message('note_off', channel=0, note=note, velocity=64, time=EIGHTH_NOTE))

    return track


def pick_scale(hue):
    if 0 <= hue < 43:
        scale = SCALES['C_major']
    elif 43 <= hue < 86:
        scale = SCALES['D_major']
    elif 86 <= hue < 129:
        scale = SCALES['A_minor']
    elif 129 <= hue < 172:
        scale = SCALES['B_minor']
    elif 172 <= hue < 215:
        scale = SCALES['E_minor']
    else:
        scale = SCALES['G_major']

    return scale
