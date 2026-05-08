import numpy as np
import cmath as cp
from scipy.io import wavfile as waw
import matplotlib.pyplot as plt
import cmath as cm

""""
#Komplexa tal:
#inbyggt i python z = 2 + 3j

#Polär form:
(r,phi) = cmath.polar(z)
cmath retunerar komplexa tal
Använd scipy.io.wavfile för att läsa och skriva ljdufiler
ex på användning: rate, data = waw.read('Piano_1.wav')
ex på skriva ljudfil: wav.write("my_sound.waw", rate, data)
viktigt att hålla koll på vilket waw format man avänder(int, flytal, mm)
LJUDEFFEKTER:
    rate, data = waw.read('Piano_1.wav')
    N = Numer_of_datapoints = len(data)
    plt.figure()
    plt.plot(data)
    plt.show()

    EKO:
    index = (int(N/4))
    data[index:] += (0.5*data[0:-index]).astype("int")
    data[2*index:] += (0.25*data[0:-2*index]).astype("int")
Fouriertransform-frekvensdomän finns i numpy
Den diskreta fouriertransformen tar en diskret signal och transformerar till vektor med frekvenser
from scipy import fft,ifft
freequency_data = fft(x) 
x = ifft(frequency_data).  x blir komplext

Ta medelvärde av RGB för att få svartvit bild

Faltning med Gauss kärna

luffyBlur = scipy.signal.convolve2d(luffy,kernalGauss, mode = "same")
"""

#UPG 1 a)

def mandelbrot(c):
    max_iter = 100
    z = 0
    for i in range(max_iter):
        z = z*z + c
    if abs(z) > 2:
        return False
    return True

#UPG 1b)

def zero_matrix():
    s = (401,401)
    M = np.zeros(s)

a = np.arange(-2,2,0.01)
b = np.arange(-2,2,0.01)

A, B = np.meshgrid(a, b)
C = A + 1j * B

result = mandelbrot(C)

M = result.astype(int)

# Visa bild
plt.imshow(M, cmap='gray')
plt.xlabel('a')
plt.ylabel('b')
plt.title('Mandelbrot')
plt.show()



