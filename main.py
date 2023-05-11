from pydub import AudioSegment
from pydub.playback import play


def openAudio(file: str):
    if file[-3:] == 'mp3':
        return AudioSegment.from_mp3(file)
    elif file[-3:] == 'wav':
        return AudioSegment.from_wav(file)

