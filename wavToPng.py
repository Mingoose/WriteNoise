import scipy.io.wavfile
import math
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x): # condense variables down to 0<x<1   
    if x < -700:
        x = -700
 
    ans = 1/(1 + math.e ** (-x))
    
    return ans
        
def soundToColor(x):
    a = x//256
    b = x%256
    a = min(a,255)
    b = min(b,255)
    a = int(a)
    b = int(b)
    return a,b




out = scipy.io.wavfile.read("rickroll.wav", mmap=False) # read file
a,b = out
print(out)
#plt.plot(b, label="Sound Data")
#plt.legend()
#plt.xlabel("Time [s]")
#plt.ylabel("Amplitude")
#plt.show()
list1 = b.tolist()
list2 = []

if isinstance(list1[0],list): # if 2d array average elements in subarrays to make 1d array
    for i in range(len(list1)):
        total = 0
        for j in range(len(list1[i])):
            total += list1[i][j]
        list2.append(total/len(list1[i]))
        
if isinstance(list1[0],list):
    list1 = list2
    


#for i in range(len(list1)):
#    list1[i] = int(255*sigmoid(list1[i])) # compressing array down to 0<x255

#for i in range(len(list1)):
 #   list1[i] += 32768
  #  print(list1[i])





img = Image.new('RGB',(300,300)) # image creation -- 300,300 is arbitrary
pixels = img.load()
count = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r,g = soundToColor(list1[count])
        b,a = soundToColor(list1[count])
        pixels[i,j] = (r,g,b,a) # setting rgb values equal to values from list1
        count += 2
print("done")
img.show()
