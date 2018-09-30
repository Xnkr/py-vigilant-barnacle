import matplotlib.pyplot as plt
from skimage import io 
import numpy as np
from scipy import fftpack
img = io.imread('rice.png')
# img = arr = np.asarray(amg)
print img
_dct = fftpack.dct(fftpack.dct(img.T,norm="ortho").T,norm="ortho")
print _dct
plt.imshow(_dct, vmin=0, vmax=1, cmap=plt.get_cmap('gray'))
plt.show()