import numpy as np
import zarr 
import gc

from Specgram import *
from USV import *
from Detection import *
from functions import *


fs, x = load_audio_file()
spec = Specgram(x, fs)
spec.genSpec()
# spec.pltSpec()
S = spec.spec
sizeX = int(spec.getTimeLen())
sizeY = int(spec.getFreqLen())


store = zarr.DirectoryStore('data/example.zarr')
root = zarr.group(store)
hello = root.create_dataset('hello', shape=(10000, 10000), chunks=(1000,1000), dtype=np.float32)


# z1 = zarr.open('data/example.zarr', mode='w', shape=(sizeY, sizeX), 
#                 chunks=(sizeY,None), dtype=np.float32)
# print(z1.chunks)
# z1[:] = S
# z2 = zarr.open('data/example.zarr', mode='r')
# print(np.all(z1[:] == z2[:]))

# size = int(10000)
# z1 = zarr.open('data/example.zarr', mode='w', shape=(size, size), 
#                chunks=(size/100, size/100), dtype='i4')
# z2 = zarr.open('data/example.zarr', mode='r')
# print(np.all(z1[:] == z2[:]))

# z1.append(S, axis=1)
# z1.shape

# del z1
# gc.collect()