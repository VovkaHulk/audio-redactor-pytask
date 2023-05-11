import pydub.effects
from pydub import AudioSegment
from pydub.playback import play


def open_audio(file: str):
    if file[-3:] == 'mp3':
        return AudioSegment.from_mp3(file)
    elif file[-3:] == 'wav':
        return AudioSegment.from_wav(file)


def change_volume(segment: AudioSegment, value, start=0, end=0):
    if end == 0:
        end = len(segment)
    slice = segment[start:end]
    slice += value
    return segment[:start] + slice + segment[end:]


def change_speed(segment: AudioSegment, value, start=0, end=0):
    if end == 0:
        end = len(segment)
    slice = segment[start:end]
    slice = pydub.effects.speedup(slice, value)
    return segment[:start] + slice + segment[end:]
