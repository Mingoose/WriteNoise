import averageAmplitude
import frequency
import math

def makeWaves(pixels, squareDimension, amplitude, frequency):
    dividedRowNum = squareDimension / 3
    for j in (0, squareDimension):
        i = int(amplitude / 10 * math.sin(frequency * j) + dividedRowNum)
        transparencyValue = pixels[i,j][3]
        if (transparencyValue in range(129,255)):
            transparencyValue = 129
        elif (transparencyValue in range(0,128)):
            transparencyValue = 128

        i = int(amplitude / 10 * math.sin(frequency * j) + dividedRowNum * 2)
        transparencyValue = pixels[i,j][3]
        if (transparencyValue in range(129,255)):
            transparencyValue = 129
        elif (transparencyValue in range(0,128)):
            transparencyValue = 128