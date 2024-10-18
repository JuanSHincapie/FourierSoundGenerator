import sounddevice as sd
import numpy as np

def play_sound(signal, sample_rate, device_index = 11):
    try:
        signal = np.asarray(signal, dtype=np.float32)
        print(f"Usando el dispositivo: {sd.query_devices(device_index)['name']}")
        print(f"Frecuencia de muestreo: {sample_rate} Hz")        
        
        sd.play(signal, sample_rate, device=device_index)
        sd.wait()  
    except Exception as e:
        print(f"Error al reproducir sonido: {e}")