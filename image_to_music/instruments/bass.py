import mido
from mido import Message, MidiTrack
from image_to_music.music_settings import EIGHTH_NOTE


def create_bass(hsv_array, tempo):
    track = MidiTrack()
    track.append(mido.Message('program_change', program=34, time=0))
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(2):
        for row in hsv_array:
            for pixel in row:
                hue, sat, val = pixel
                sat = 50 + round(sat / 10)

                for _ in range(8):
                    track.append(Message('note_on', channel=0, note=sat-12, velocity=64, time=0))
                    track.append(Message('note_off', channel=0, note=sat-12, velocity=64, time=EIGHTH_NOTE))

    return track
