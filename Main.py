import numpy as np
from scipy.io import wavfile as waw
from scipy import ndimage
import matplotlib.pyplot as plt
import cmath as cm
import scipy as sc

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

#print(zero_matrix)


#A = 1 + 1j
#print(mandelbrot(A))

#Fråga 1b)
def function_b(): # skapar en bild av mandelbrotmängden
    a = np.linspace(-2,2,400) 
    b = np.linspace(-2,2,400)
    amin = -2
    amax = 2
    bmin = -2
    bmax = 2
    s = (401,401)
    M = np.zeros(s) # skapar en nollmatris som vi kommer att fylla i med 1:or där mandelbrotmängden finns
    for A in range(len(a)):
        for B in range(len(b)):
            resultat = a[A] + b[B]*1j # skapar det komplexa talet som vi ska testa
            if(mandelbrot(resultat)):
                M[int((a[A]+2)*100), int((b[B]+2)*100)] = 1 # fyller i 1:or i matrisen där mandelbrotmängden finns, multiplicerar med 100 för att få rätt index i matrisen
    plt.imshow(M, cmap='gray', extent=(amin, amax, bmin, bmax))
    plt.show()


def function_c():
    a = np.linspace(-0.9,-0.5,400) 
    b = np.linspace(0.0,0.4,400)
    amin = -0.9
    amax = -0.5
    bmin = 0
    bmax = 0.4
    s = (401,401)
    M = np.zeros(s) # skapar en nollmatris som vi kommer att fylla i med 1:or där mandelbrotmängden finns
    for A in range(len(a)):
        for B in range(len(b)):
            resultat = a[A] + b[B]*1j # skapar det komplexa talet som vi ska testa
            if(mandelbrot(resultat)):
                M[int((a[A]+2)*100), int((b[B]+2)*100)] = 1 # fyller i 1:or i matrisen där mandelbrotmängden finns, multiplicerar med 100 för att få rätt index i matrisen
    plt.imshow(M, cmap='gray', extent=(amin, amax, bmin, bmax))
    plt.show()


def read_image():
    bild = plt.imread("IMG_8625.jpeg")
    # Convert to grayscale by taking mean across RGB channels
    svartbild = np.mean(bild, axis=2)
    #plt.imshow(svartbild, cmap = "gray")
    #plt.show()
    return svartbild


def sobel_image():
    svartbild = read_image()

    Gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]])

    xd = ndimage.convolve(svartbild, Gx, mode='constant')
    yd = ndimage.convolve(svartbild, Gy, mode='constant')
    S = np.sqrt(xd**2 + yd**2)

    #plt.imshow(S, cmap='gray')
    #plt.show()
    return S


def reverse_falt():
    S = sobel_image()
    vilkor = S > 100
    S[vilkor] = 0
    S[~vilkor] = 255
    plt.imshow(S, cmap='gray')
    plt.show()

reverse_falt()

dsagdsa
