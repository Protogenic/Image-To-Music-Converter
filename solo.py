import mido
from mido import Message, MidiFile, MidiTrack

scales = {
    'C_major': [60, 62, 64, 65, 67, 69, 71, 72],
    'D_major': [62, 64, 66, 67, 69, 71, 73, 74],
    'G_major': [67, 69, 71, 72, 74, 76, 78, 79],
    'A_minor': [69, 71, 72, 74, 76, 77, 79, 81],
    'B_minor': [71, 73, 74, 76, 78, 79, 81, 83],
    'E_minor': [64, 66, 67, 69, 71, 72, 74, 76]
}

sixteenth_note = 120
eighth_note = 240
quarter_note = 480


def create_solo(tempo, hsv_array, hue):
    scale = []
    if 0 <= hue < 43:
        scale = scales['C_major']
    elif 43 <= hue < 86:
        scale = scales['D_major']
    elif 86 <= hue < 129:
        scale = scales['A_minor']
    elif 129 <= hue < 172:
        scale = scales['B_minor']
    elif 172 <= hue < 215:
        scale = scales['E_minor']
    else:
        scale = scales['G_major']

    track = MidiTrack()
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    track.append(Message('program_change', program=29, channel=0))
    track.append(Message('control_change', control=7, value=120, time=0))

    empty_border = 20
    for row in hsv_array:
        for pixel in row:
            value = pixel[0]
            if value < empty_border:
                track.append(Message('note_off', channel=0, note=0, velocity=64, time=eighth_note))
            else:
                index = int(((value - empty_border) / (255 - empty_border)) * (len(scale) - 1))
                note = scale[index]
                track.append(Message('note_on', channel=0, note=note, velocity=64, time=0))
                track.append(Message('note_off', channel=0, note=note, velocity=64, time=eighth_note))

    return track
