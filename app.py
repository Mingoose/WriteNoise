from flask import Flask, render_template, url_for, request, send_file
import scipy.io.wavfile
import math
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
app = Flask(__name__)
os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generic', methods = ['POST', 'GET'])
def generic():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save('input.wav')
            wavtoPNG('input.wav')
        return render_template('generic.html')
    return render_template('generic.html')

def wavtoPNG(wavfile):
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

    def stupidBinary(x):
        print(type(x),file=sys.stderr)
        r = "0b"
        g = "0b"
        b = "0b"
        a = 255
        r += x[-9] + x[-6] + x[-12] + x[-15] + x[-1] + "0"*3
        g += x[-8] + x[-5] + x[-11] + x[-14] + x[-3] + "0"*3
        b += x[-7] + x[-4] + x[-10] + x[-13] + x[-2] + "0"*3
        if x[0] == "-":
            a = 128
        r = int(r,2)
        g = int(g,2)
        b = int(b,2)
        return(r,g,b,a)


    out = scipy.io.wavfile.read(wavfile, mmap=False) # read file
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
    

    for i in range(len(list1)):#turn list into binary
        list1[i] = bin(int(list1[i]))
        indB = list1[i].index("b") + 1
        binary = list1[i][indB:]
        binary = binary.zfill(16)
        list1[i] = list1[i][:indB] + binary
    
    
#for i in range(len(list1)):
#    list1[i] = int(255*sigmoid(list1[i])) # compressing array down to 0<x255

#for i in range(len(list1)):
 #   list1[i] += 32768
   

    img = Image.new('RGBA',(300,300)) # image creation -- 300,300 is arbitrary
    pixels = img.load()
    count = 0

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            (r,g,b,a) = stupidBinary(list1[count])
            pixels[i,j] = (r,g,b,a) # setting rgb values equal to values from list1
            count += 1
        

    print("done")
    img.show()
    img.save("output.png")
    # send_file('output.png', as_attachment=True, attachment_filename='output_photo.png')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)