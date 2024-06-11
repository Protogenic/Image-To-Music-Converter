from typing import Annotated
from PIL import Image
from io import BytesIO
import numpy as np
import base64

import mido
from mido import Message, MidiFile, MidiTrack

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from drum_patterns import punk, eighth, classic
from chords import majorChord, minorChord
from solo import create_solo

app = FastAPI()
templates: Jinja2Templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

sixteenth_note = 120
eighth_note = 240
quarter_note = 480

@app.post("/uploadfile/", response_class=HTMLResponse)
async def create_upload_files(file: UploadFile, request: Request):
    extension = file.filename.split(".")[-1]
    if not extension in {"jpg", "jpeg", "png"}:
        return {"message": "Wrong file extension"}

    source_image = Image.open(file.file)
    source_image.save("static/image." + 'jpg')
    data = BytesIO()
    img_str = base64.b64encode(data.getvalue()).decode()
    
    image_for_chords = source_image.resize((4, 4))
    
    resized_image = BytesIO()
    if extension == 'jpg':
        extension = 'jpeg'
    image_for_chords.save(resized_image, format=extension)
    hsv_array_for_chords = np.array(image_for_chords.convert('HSV'))

    hue_4x4 = hsv_array_for_chords[:, :, 0].mean()
    saturation_4x4 = hsv_array_for_chords[:, :, 1].mean()
    value_4x4 = hsv_array_for_chords[:, :, 2].mean()

    tempo = round(value_4x4 * 0.5 + 60)

    midi_file = MidiFile()

    track_chords = MidiTrack()
    track_chords.append(Message('program_change', program=30, channel=0)) # Distortion Guitar
    midi_file.tracks.append(track_chords)
    track_chords.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    track_chords.append(Message('control_change', control=7, value=50, time=0))

    track_bass = MidiTrack()
    track_bass.append(mido.Message('program_change', program=34, time=0))
    midi_file.tracks.append(track_bass)

    tracks = []
    if tempo < 100:
        tracks = classic(tempo)
    elif 100 <= tempo <= 160:
        tracks = eighth(tempo)
    else :
        tracks = punk(tempo)

    for track in tracks:
        midi_file.tracks.append(track)

    image_for_solo = source_image.resize((16, 16))
    hsv_array_for_solo = np.array(image_for_solo.convert('HSV'))
    solo_track = create_solo(tempo, hsv_array_for_solo, hue_4x4)
    midi_file.tracks.append(solo_track)

    for _ in range(2):
        for row in hsv_array_for_chords:
            for pixel in row:
                hue, sat, val = pixel
                sat = 50 + round(sat / 10)

                if 0 <= hue < 86 or 215 <= hue <= 255:
                    for _ in range(4):
                        majorChord(sat, quarter_note, track_chords)
                else:
                    for _ in range(4):
                        minorChord(sat, quarter_note, track_chords)

                for _ in range(4):
                    track_bass.append(Message('note_on', channel=0, note=sat-12, velocity=64, time=0))
                    track_bass.append(Message('note_off', channel=0, note=sat-12, velocity=64, time=quarter_note))

    midi_file.save("static/music.mid")

    return templates.TemplateResponse("post.html", {"request": request,
                                                    "img_data": img_str,
                                                    "tempo": tempo,
                                                    "file_name": "static/music.mid",
                                                    "extension": extension})


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
