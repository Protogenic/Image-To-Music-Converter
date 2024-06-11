import mido
from mido import Message, MidiFile, MidiTrack

# константы в upper кейсе все должны быть
sixteenth_note = 120
eighth_note = 240
quarter_note = 480

BASS_SEQUENCE_FIRST_PART = [  # вообще можно в отдельный файл с анстройками музыки типа вынести
    Message('note_on', note=36, velocity=100, time=0, channel=9),
    Message('note_off', note=36, velocity=100, time=sixteenth_note*8, channel=9),
    Message('note_on', note=36, velocity=100, time=0, channel=9),
    Message('note_off', note=36, velocity=100, time=sixteenth_note*2, channel=9),
    Message('note_on', note=36, velocity=100, time=0, channel=9),
    Message('note_off', note=36, velocity=100, time=sixteenth_note*6, channel=9),
]

# названия функций должны быть с глаголами - так как это экшен
def punk(tempo):
    tracks = []

    bass_drum = MidiTrack()
    snare_drum = MidiTrack()
    cymbals = MidiTrack()

    bass_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    snare_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    cymbals.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(32):
        #  с кучи таких добавлений орнул, сорри
        # вынеси эту структуру в глобальный список или кортеж на уровень файла, и используй предподготовленные данные
        # аля посмотри выше пример накидаю и тут уже bass_drum.extend(BASS_SEQUENCE_FIRST_PART)
        # вообщем везде убирай и рефактори эти кучи добавлений
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=sixteenth_note*8, channel=9))
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=sixteenth_note*2, channel=9))
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=sixteenth_note*6, channel=9))

    for _ in range(64):
        snare_drum.append(Message('note_off', note=38, velocity=100, time=sixteenth_note*4, channel=9))
        snare_drum.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
        snare_drum.append(Message('note_off', note=38, velocity=100, time=sixteenth_note*4, channel=9))

    for _ in range(32):
        cymbals.append(Message('note_on', note=49, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=49, velocity=100, time=quarter_note, channel=9))
        cymbals.append(Message('note_on', note=46, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=46, velocity=100, time=quarter_note, channel=9))
        cymbals.append(Message('note_on', note=46, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=46, velocity=100, time=quarter_note, channel=9))
        cymbals.append(Message('note_on', note=46, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=46, velocity=100, time=quarter_note, channel=9))

    tracks.append(bass_drum)
    tracks.append(snare_drum)
    tracks.append(cymbals)

    return tracks


def eighth(tempo):
    tracks = []

    bass_drum = MidiTrack()
    snare_drum = MidiTrack()
    cymbals = MidiTrack()

    bass_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    snare_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    cymbals.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(64):
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=quarter_note*2, channel=9))

    for _ in range(64):
        snare_drum.append(Message('note_off', note=38, velocity=100, time=eighth_note * 2, channel=9))
        snare_drum.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
        snare_drum.append(Message('note_off', note=38, velocity=100, time=eighth_note * 2, channel=9))

    for _ in range(64):
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=sixteenth_note, channel=9))
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=sixteenth_note, channel=9))
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=sixteenth_note, channel=9))
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=eighth_note, channel=9))
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=sixteenth_note, channel=9))
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=sixteenth_note, channel=9))
        cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=42, velocity=100, time=sixteenth_note, channel=9))

    tracks.append(bass_drum)
    tracks.append(snare_drum)
    tracks.append(cymbals)

    return tracks


def classic(tempo):
    tracks = []

    bass_drum = MidiTrack()
    snare_drum = MidiTrack()
    cymbals = MidiTrack()

    bass_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    snare_drum.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))
    cymbals.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    for _ in range(16):
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=quarter_note*5, channel=9))
        bass_drum.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
        bass_drum.append(Message('note_off', note=36, velocity=100, time=quarter_note * 3, channel=9))

    for _ in range(32):
        snare_drum.append(Message('note_off', note=38, velocity=100, time=quarter_note * 2, channel=9))
        snare_drum.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
        snare_drum.append(Message('note_off', note=38, velocity=100, time=quarter_note * 2, channel=9))

    for _ in range(16):
        cymbals.append(Message('note_on', note=46, velocity=100, time=0, channel=9))
        cymbals.append(Message('note_off', note=46, velocity=100, time=eighth_note, channel=9))
        for _ in range(15):
            cymbals.append(Message('note_on', note=42, velocity=100, time=0, channel=9))
            cymbals.append(Message('note_off', note=42, velocity=100, time=eighth_note, channel=9))

    tracks.append(bass_drum)
    tracks.append(snare_drum)
    tracks.append(cymbals)

    return tracks
