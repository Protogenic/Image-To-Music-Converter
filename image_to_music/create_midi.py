from PIL import Image
from io import BytesIO
import numpy as np

import mido
from mido import Message, MidiFile, MidiTrack

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from image_to_music.instruments.drum_patterns import create_drums
from image_to_music.instruments.solo import create_solo
from image_to_music.instruments.chords import create_chords_track
from image_to_music.instruments.bass import create_bass


def create_music_file(image):
    midi_file = MidiFile()

    hsv_array_for_solo, hsv_array_for_chords = create_hsv_arrays(image)

    hue_4x4 = hsv_array_for_chords[:, :, 0].mean()
    value_4x4 = hsv_array_for_chords[:, :, 2].mean()
    tempo = round(value_4x4 * 0.5 + 60)

    solo_track = create_solo(tempo, hsv_array_for_solo, hue_4x4)
    midi_file.tracks.append(solo_track)

    chords_track = create_chords_track(hsv_array_for_chords, hue_4x4, tempo)
    midi_file.tracks.append(chords_track)

    bass_track = create_bass(hsv_array_for_chords, tempo)
    midi_file.tracks.append(bass_track)

    drum_tracks = create_drums(tempo)
    for track in drum_tracks:
        midi_file.tracks.append(track)

    midi_file.save("static/music.mid")


def create_hsv_arrays(image):
    hsv_array_for_solo = np.array(image.resize((16, 16)).convert('HSV'))
    hsv_array_for_chords = np.array(image.resize((4, 4)).convert('HSV'))

    return hsv_array_for_solo, hsv_array_for_chords
