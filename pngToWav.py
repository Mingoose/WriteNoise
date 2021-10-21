import scipy.io.wavfile
import math
from PIL import Image
import numpy
def revSigmoid(x): # turning values from [0,255] to all real numbers (i think)
    
    if x == 0:
        return -700
    
    ans = -numpy.log(255/x - 1)
    
    return ans
list1  = []
img = Image.open("richard.png")
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        (r,g,b,a) = pixels[i,j] #set r,g,b to values from list1
        list1.append(revSigmoid(r))
        list1.append(revSigmoid(g))
        list1.append(revSigmoid(b))
arr = numpy.array(list1)
bitrate = 48000 #cant extract from image in given version
scipy.io.wavfile.write("reverse2.wav",bitrate,arr)
