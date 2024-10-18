import numpy as np

def generate_riff(freqs, sample_rate, note_duration):
    t = np.linspace(0, note_duration, int(sample_rate * note_duration), endpoint=False)   
    signal = np.array([])

    for freq in freqs:
        fundamental = 0.5 * np.sin(2 * np.pi * freq * t)
        harmonic1 = 0.3 * np.sin(2 * np.pi * freq * 2 * t) 
        harmonic2 = 0.2 * np.sin(2 * np.pi * freq * 3 * t) 
        note_signal = fundamental + harmonic1 + harmonic2
        signal = np.concatenate((signal, note_signal))
    
    return signal, sample_rate
