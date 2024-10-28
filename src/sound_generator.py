import numpy as np
import random


def karplus_strong(freq, sample_rate, duration):
      
    n_samples = int(sample_rate * duration)
    buffer_size = int(sample_rate / freq)

    buffer = np.random.uniform(-1, 1, buffer_size)
    signal = np.zeros(n_samples)
   
    for i in range(n_samples):
        signal[i] = buffer[i % buffer_size]
        avg = 0.5 * (buffer[i % buffer_size] + buffer[(i + 1) % buffer_size]) # complejidad : n
        buffer[i % buffer_size] = avg * 0.995 

    return signal

def apply_adsr(signal, sample_rate, attack=0.01, decay=0.1, sustain=0.7, release=0.1):
    
    n_samples = len(signal)
    t = np.linspace(0, n_samples / sample_rate, n_samples)

    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)
    sustain_samples = n_samples - (attack_samples + decay_samples + release_samples)  #complejidad O(1)

    env = np.concatenate([
        np.linspace(0, 1, attack_samples),               # Attack
        np.linspace(1, sustain, decay_samples),           # Decay
        np.full(sustain_samples, sustain),                 # Sustain
        np.linspace(sustain, 0, release_samples)          # Release
    ])

    return signal * env[:n_samples]

def generate_riff(chord_freqs_list, sample_rate, note_duration):
    signal = np.array([])

    for chord_freqs in chord_freqs_list:
        chord_signal = np.zeros(int(sample_rate * note_duration))
        
        for freq in chord_freqs:
            note_signal = karplus_strong(freq, sample_rate, note_duration)
            note_signal = apply_adsr(note_signal, sample_rate)  # Complejidad: n^2
            chord_signal += note_signal
        
        
        chord_signal /= np.max(np.abs(chord_signal) + 1e-7)
       
        signal = np.concatenate((signal, chord_signal))
    
    return signal, sample_rate