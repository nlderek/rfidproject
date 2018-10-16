import sys
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean

a= Image.open(os.getcwd() + '\\recognimage\\images\\numbers\\0.1.png')
width, height = a.size
pixel_values = numpy.array(pixel_values).reshape((width, height, 3)

print (pixel_values)
#b = np.asarray(a)
#c = b[0]
#d = c[2,0]

#print(d)


