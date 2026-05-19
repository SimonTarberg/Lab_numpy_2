import numpy as np
from scipy.io import wavfile as waw
from scipy import ndimage
import matplotlib.pyplot as plt
import cmath as cm
import scipy as sc
from scipy import fft

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
    """Return True if c stays bounded in the Mandelbrot iteration."""
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

function_c()

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


def plot_sound_wawe():
    rate, data = waw.read("Piano_1_C.wav")
    N = len(data)
    data = data[0:N]
    duration = N / rate
    time = np.linspace(0., duration, N)
    plt.figure()
    plt.plot(time, data)
    plt.ylabel("Amplitud")
    plt.xlabel("Tid (s)")
    plt.title("Ljudvåg: Piano_1_C.wav")
    plt.grid(True)
    plt.show()


def fourier_transform():
    rate, data = waw.read("Piano_1_C.wav")
    if data.ndim > 1:
        data = data[:, 0]
    N = len(data)

    # Compute Fourier transform and plot magnitude of the first half
    F = fft.fft(data)
    half = N // 2
    freqs = np.arange(half) * rate / N

    plt.figure()
    plt.plot(freqs, np.abs(F[:half]))
    plt.title("Magnitud av Fouriertransformen")
    plt.xlabel("Frekvens (Hz)")
    plt.ylabel("amplitud")
    plt.grid(True)
    plt.show()

def find_tune(frequenzy):
    notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}
    for i in range(1, 5):  # Kontrollera harmoniska övertoner upp till 4:e ordningen
        for note, freq in notes.items():
            if abs(freq * i - frequenzy) < 5:  # Tolerans för tonigenkänning
                return note
    return "Unknown"

def read_sound(file):
    """Läser in en ljudfil, väljer kanal vid stereo och hittar huvudfrekvensen."""
    rate, data = waw.read(file)
    if data.ndim > 1:
        data = data[:, 0]  # Använder första kanal vid stereo
    freq_max = np.argmax(np.abs(fft.fft(data)))

    return freq_max, find_tune(freq_max)
