import numpy as np
from scipy.signal import argrelextrema

def averageAmplitude(numPyArray):
# for local maxima
    listOfMaxs = numPyArray[argrelextrema(numPyArray, np.greater)[0]]
    print(listOfMaxs)
    average = sum(listOfMaxs) / len(listOfMaxs)
    print (average)
    return average
    


