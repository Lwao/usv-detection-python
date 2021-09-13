from scipy.io import wavfile
from tkinter import filedialog
from scipy import signal

import numpy as np

from Specgram import *
from USV import *
from Detection import *


def load_audio_file():
    # filename = filedialog.askopenfilename(
    #     title='Please select valid audio files.', 
    #     filetypes=[('Audio Files', ['.wav', '.flac', '.mp3'])])
    # if not filename: return None
    filename = 'C:/Users/levyg/Desktop/usv_audio.wav'
    samplerate, data = wavfile.read(filename)
    return samplerate, data

def usv_detection():
    None

# fs, x = load_audio_file()
# spec = Specgram(x, fs)
# spec.genSpec()
# spec.pltSpec()
# S = spec.spec
# t = spec.t
# f = spec.f


# implement step and win
# ensure min. deltaF and min. deltaT