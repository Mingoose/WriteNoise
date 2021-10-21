import scipy.io.wavfile
import math
from PIL import Image
import numpy
#def revSigmoid(x): # turning values from [0,255] to all real numbers (i think)
 #   
  #  if x == 0:
   #     return -700
    #
    #ans = -numpy.log(255/x - 1)
    #return ans
#def colorToSound(a,b):
 #   out = a * 256 + b
  #  out = out - 32768
   # return out
def dumberBinary(r,g,b,a):
    out = "0b0"
    if a == 128:
        out = "-0b"
    r = bin(r)[2:]
    g = bin(g)[2:]
    b = bin(b)[2:]
    r = r.zfill(8)
    g = g.zfill(8)
    b = b.zfill(8)
    out += r[3] + g[3] + b[3] + r[2] + g[2] + b[2] + r[0] + g[0] + b[0] + r[1] + g[1] + b[1] + g[4] + b[4] + r[4]
    out = int(out,2)
    return out
list1  = []
img = Image.open("praying1.png")
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        (r,g,b,a) = pixels[i,j] #set r,g,b,a to values from list1
        list1.append((dumberBinary(r,g,b,a)))
for i in range(len(list1)):
    list1[i] = float(list1[i])
print(list1[1000:2000])
arr = numpy.array(list1)
print(arr)
bitrate = 48000 #cant extract from image in given version
scipy.io.wavfile.write("gate.wav",bitrate,arr)
