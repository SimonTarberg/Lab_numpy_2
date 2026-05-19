import numpy as np
from scipy.io import wavfile as waw
from scipy import ndimage
import matplotlib.pyplot as plt
import cmath as cm
import scipy as sc
from scipy import fft


def dur_till_moll_ackord(fil):
    """Ska flytta grundtonen E(och dess övertoner) till Eb"""
    rate, data = waw.read(fil)
    if data.ndim > 1:
        data = data[:, 0] #ifall stereo ljud --> mono
    N = len(data)
    F = fft.fft(data) #gör den till ....

    F_original = F.copy() #skapar kopia av F

    halva_F = N // 2
    bredd_av_ton = 20
    duration = N / rate

    # Grundfrekvenser för ändring
    frekvens_E = 329.63   #E
    frekvens_Eb = 311.13  #Eb

    # Flytta grundtonen samt de 3 första övertonerna
    for i in range(1, 5):
        # Beräkna index i Fouriertransforms-vektorn för övertonerna
        index_e = int(frekvens_E * i * duration)
        index_eb = int(frekvens_Eb * i * duration)

        F[index_eb - bredd_av_ton: index_eb + bredd_av_ton] = F[index_e - bredd_av_ton: index_e + bredd_av_ton]
        F[index_e - bredd_av_ton: index_e + bredd_av_ton] = 0

    #skapar spegelbild av
    tom_plats = len(F[halva_F + 1:])

    #np.flip för att spegla andra halvan
    #np.conj för att tecknet på den imaginära delen ska bytas ut
    spegelbild = np.conj(np.flip(F[1:halva_F + 2]))[:tom_plats]
    F[halva_F + 1:] = spegelbild

    # transform tillbaks till ljud (invers av Fouriertransform)
    moll_data = fft.ifft(F).real

    frekvens_axel = np.arange(halva_F) / duration
    magnitud_original = np.abs(F_original[:halva_F])
    magnitud_moll = np.abs(F[:halva_F])

    plt.figure(figsize=(11, 6))
    plt.plot(frekvens_axel, magnitud_moll, label="C-moll", color="red")
    plt.plot(frekvens_axel, magnitud_original, label="C-dur", color="blue")

    plt.title("Från C-dur till C-moll")
    plt.legend()
    plt.xlabel("Frekvens (Hz)")
    plt.ylabel("Amplitud (styrka)")
    plt.xlim(200, 1500)

    plt.show()

    # normalisera ljudet så det inte klipper
    moll_data_normaliserat = (moll_data / np.max(np.abs(moll_data))) * 0.9

    # spara det nya moll ackordet som en ljudfil
    waw.write("Cmoll_output.wav", rate, moll_data_normaliserat.astype(np.float32))



dur_till_moll_ackord("Cdur.wav")