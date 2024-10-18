from generator import generate_sine_wave
from viusalizer import plot_time_domain, plot_frequency_domain
from player import play_sound
from guitar_generator import generate_riff


def main():
    sample_rate = 48000      
    #frequency = 440  #<--- Esta la dejo por si queremos generar solo 1 MIIIIP
    freqs = [440, 493.88, 523.25, 587.33]
    duration = 0.5
    signal, _ = generate_riff(freqs, sample_rate, duration)

    plot_time_domain(signal, sample_rate)
    plot_frequency_domain(signal, sample_rate)

    print("Acá inicia el sample")
    play_sound(signal, sample_rate, device_index=11)


if __name__ == "__main__":
    main()