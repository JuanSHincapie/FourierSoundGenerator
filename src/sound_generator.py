import numpy as np
import random


def karplus_strong(freq, sample_rate, duration):
      
    n_samples = int(sample_rate * duration)
    buffer_size = int(sample_rate / freq)

    buffer = np.random.uniform(-1, 1, buffer_size)
    signal = np.zeros(n_samples)
   
    for i in range(n_samples):
        signal[i] = buffer[i % buffer_size]
        avg = 0.5 * (buffer[i % buffer_size] + buffer[(i + 1) % buffer_size])
        buffer[i % buffer_size] = avg * 0.995 

    return signal

def generate_riff(chord_freqs_list, sample_rate, note_duration):
    signal = np.array([])

    for chord_freqs in chord_freqs_list:
        chord_signal = np.zeros(int(sample_rate * note_duration))
      
        for freq in chord_freqs:
            note_signal = karplus_strong(freq, sample_rate, note_duration)
            chord_signal += note_signal
       
        chord_signal /= np.max(np.abs(chord_signal) + 1e-7)
      
        signal = np.concatenate((signal, chord_signal))
    
    return signal, sample_rate
