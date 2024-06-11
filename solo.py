import mido
from mido import Message, MidiFile, MidiTrack

g_major_scale = [43, 45, 47, 48, 50, 52, 54, 55, 55, 57, 59, 60, 62, 64, 66, 67]
e_minor_scale = [47, 48, 50, 52, 54, 55, 57, 59, 59, 60, 62, 63, 64]

sixteenth_note = 120
eighth_note = 240
quarter_note = 480


def create_solo(tempo, hsv_array):
    scale = g_major_scale

    track = MidiTrack()
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    track.append(Message('program_change', program=29, channel=0))
    track.append(Message('control_change', control=7, value=120, time=0))

    empty_border = 30
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
