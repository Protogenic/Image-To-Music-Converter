import mido
import pytest
from PIL import Image

from image_to_music.create_midi import create_music_file


def test_midi():
    image_processed = Image.open("static/test/image.jpg")
    create_music_file(image_processed)
    midi_processed = mido.MidiFile("static/test/music.mid")
    midi_test = mido.MidiFile("static/test/music.mid")
    assert compare_midi_files(midi_processed, midi_test)


def compare_midi_files(midi_processed, midi_test):
    if len(midi_processed.tracks) != len(midi_test.tracks):
        return False

    for i, track in enumerate(midi_processed.tracks):
        if len(track) != len(midi_test.tracks[i]):
            return False
        for message1, message2 in zip(track, midi_test.tracks[i]):
            if message1 != message2:
                return False
    return True
