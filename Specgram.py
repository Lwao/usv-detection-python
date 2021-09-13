import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.cbook as cbook

from scipy import signal
from scipy.fft import fftshift


class Specgram:
    # Initializing
    def __init__(self, audio_data=np.array([], dtype=np.int16), 
                 sampling_frequency=0, 
                 time_range=None, 
                 frequency_range=None):
        self.audio_data = audio_data
        self.fs = sampling_frequency
        
        if not time_range: 
            self.t_range = [0, len(self.audio_data)]
        else:
            self.t_range = time_range
        
        if not frequency_range: 
            self.f_range = [0, self.fs/2]
        else:
            self.f_range = time_range
            
        self.spec = np.array([], dtype=np.float32)
        self.t    = np.array([], dtype=np.float32)
        self.f    = np.array([], dtype=np.float32)
        
        self.t_len    = np.uint32(0)
        self.f_len    = np.uint32(0)
        
    def getTimeLen(self): return self.t_len 
    def getFreqLen(self): return self.f_len
    def getSpec(self):    return self.spec
    def getTime(self):    return self.t
    def getFreq(self):    return self.freq
        
    def setAudioData(self, audio_data, sampling_frequency):
        self.audio_data = audio_data
        self.fs = sampling_frequency
        
    def setLimits(self, time_range=None, frequency_range=None):
        if not time_range: 
            self.t_range = [0, len(self.audio_data)/self.fs]
        else:
            self.t_range = time_range
        
        if not frequency_range: 
            self.f_range = [0, self.fs/2]
        else:
            self.f_range = time_range
        
    def genSpec(self):
        time_slice = np.array([self.t_range[0]*self.fs, self.t_range[1]*self.fs], 
                              dtype=np.int64)
        self.f, self.t, self.spec = signal.spectrogram(
                                     self.audio_data[time_slice[0]:time_slice[1]],
                                     self.fs,             # sampling frequency [Hz]
                                     mode='magnitude',    # return magnitude only
                                     return_onesided=True # return onesided spectrum
                                    )
        self.t += self.t_range[0]
        freq_slice = np.where((self.f >= self.f_range[0]) & (self.f <= self.f_range[1]))
        self.f = self.f[freq_slice]
        self.spec = self.spec[freq_slice, :][0]
        
        spec_max = self.spec.max()
        spec_min = self.spec.min()
        
        self.spec = (self.spec-spec_min)/(spec_max-spec_min) # normalize 0-1
        
        self.t_len    = np.uint32(len(self.t))
        self.f_len    = np.uint32(len(self.f))
        
    def pltSpec(self): 
        fig, ax = plt.subplots()
        
        pcm = ax.pcolormesh(self.t, self.f, self.spec, shading='gouraud', 
                       cmap='gray_r', vmin=0, vmax=1)
        fig.colorbar(pcm, ax=ax, extend='max')
        # ax.set_ylabel('Frequency [Hz]')
        # ax.set_xlabel('Time [sec]')
        #slider to adjust vmax between 0 and 1
