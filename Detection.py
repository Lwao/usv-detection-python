import numpy as np

class Detection:
    # Initializing
    def __init__(self, time_range=None, freq_range=None, 
                 time_threshold=np.float32(0), freq_threshold=np.float32(0),
                 min_interval=np.float32(0), min_duration=np.float32(0),
                 step=np.float32(0), entropy_selection='Wiener'):
        self.t_range = time_range
        self.f_range = freq_range
        self.t_thresh = time_threshold
        self.f_thresh = freq_threshold
        self.m_interval = min_interval
        self.m_duration = min_duration
        self.step = step
        self.ent_sel = entropy_selection