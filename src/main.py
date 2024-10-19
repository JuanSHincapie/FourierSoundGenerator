from viusalizer import plot_time_domain, plot_frequency_domain, create_signal
from player import play_sound
from sound_generator import generate_riff
from notes import chords_dict, notes_dict


def get_frecuencies(chord_name):
    return [notes_dict[note] for note in chords_dict[chord_name]]

def main():
    sample_rate = 48000  

    frequencies_Dm = get_frecuencies('Dm')  
    frequencies_Bb = get_frecuencies('Bb')  
    frequencies_C = get_frecuencies('C')   
    frecuencies_BbD = get_frecuencies('Bb/D')
    frecuencies_CD = get_frecuencies('C/D')


    chords_freqs = [frequencies_Dm, frecuencies_BbD, frequencies_Dm, frecuencies_BbD, frequencies_Dm, frecuencies_BbD, frecuencies_CD] #Lose yourself - Eminem standar - Guitar

    duration = 0.42
    signal, _ = generate_riff(chords_freqs, sample_rate, duration)

    plot_time_domain(signal, sample_rate)
    plot_frequency_domain(signal, sample_rate)
    create_signal([f for chord in chords_freqs for f in chord], sample_rate, duration)

    print("Acá inicia el sample")
    play_sound(signal, sample_rate, device_index=11)


if __name__ == "__main__":
    main()