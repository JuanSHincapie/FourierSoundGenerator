import matplotlib.pyplot as plt
import numpy as np

def plot_time_domain(signal, sample_rate):   
    t = np.linspace(0, len(signal) / sample_rate, num=len(signal), endpoint=False)
    plt.figure()
    plt.plot(t, signal)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Signal in Time Domain')
    plt.show()

def plot_frequency_domain(signal, sample_rate):

    fft_result = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(len(signal), 1 / sample_rate)

    half_n = len(signal)//2
    freqs = fft_freqs[:half_n]
    magnitudes = np.abs(fft_result[:half_n])

    plt.plot(freqs, magnitudes)
    plt.title('Espectro de Frecuencia')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud')
    plt.xlim(0, 2000)
    plt.show()