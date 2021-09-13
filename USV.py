"""
status:
- 'new', new detected usv with user defined margins
- 'original', only detected by algorithm
- 'adjusted', originally detected by algorithm but 
              it had its margins corrected by user

class(klasse): usv classe determined by its format
    'complex', 'inverted_u', 'split', 'short', 
    'flat', 'step_up', 'upward_ramp', 'step_down', 
    'complex_trill', 'trill', 'downward_ramp'
    
'undefined', not yet classified

Confusion matrix:
    True Positive: USV 'detected' True, 'adjusted' as detected
        self.detected == True and self.status == 'adjusted'
    False Positive: USV 'detected' True, 'adjusted' as not detected
        self.detected == False and self.status == 'adjusted'
    False Negative: USV 'new', but 'detected'
        self.detected True and self.status == 'new'
    Ture Negative: USV 'new', but not 'detected'
        self.detected False and self.status == 'new'
"""

import numpy as np

class USV:
    # Initializing
    def __init__(self, time_start=np.float32(0), 
                 duration=np.float32(0), 
                 frequency_min=np.float32(0), 
                 bandwidth=np.float32(0),
                 status='undefined'):
        self.t_start   = np.float32(time_start)
        self.duration  = np.float32(duration)
        self.f_min     = np.float32(frequency_min)
        self.bandwidth = np.float32(bandwidth)
        
        self.f_start   = np.float32(0)
        self.f_end     = np.float32(0)
        self.sinuosity = np.float32(0)
        self.am        = np.float32(0)
        
        self.status    = status
        self.klasse    = 'undefined'
        self.detected  = False
        
    def setBox(self, time_start, duration, frequency_min, bandwidth):
        self.t_start   = np.float32(time_start)
        self.duration  = np.float32(duration)
        self.f_min     = np.float32(frequency_min)
        self.bandwidth = np.float32(bandwidth)
        self.status    = 'adjusted'
        return self
    
    def getBox(self):
        return np.array([self.t_start, 
                         self.duration, 
                         self.f_min, 
                         self.bandwidth])
    
    def confirm(self):
        self.detected = True
        self.status   = 'adjusted'
    def delete(self): 
        self.detected = False
        self.status   = 'adjusted'
    
    
    # Deleting (Calling destructor)
    #def __del__(self):
    #    None