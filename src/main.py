from viusalizer import plot_time_domain, plot_frequency_domain, create_signal
from player import play_sound
from sound_generator import generate_riff
from notes import chords_dict, notes_dict


def get_frequencies(chord_name):
    return [notes_dict[note] for note in chords_dict[chord_name]]
    
def main():
    sample_rate = 48000  
    bpm = 120 
    base_note_duration = (60 / bpm )/2 
    
    chords_with_repetitions = [
    ('Am', 2),  
    ('Dm', 2),  
    ('Am', 2),  
    ('E7', 2), 
    ('Am', 2),  
    ('G', 2),   
    ('F', 2),   
    ('E', 2),   
    ]  
    chords_freqs = []    

    for chord, repetitions in chords_with_repetitions:
        chord_freqs = get_frequencies(chord)
        chords_freqs.extend([chord_freqs] * repetitions)
       
   
    signal, _ = generate_riff(chords_freqs, sample_rate, base_note_duration)
   
    plot_time_domain(signal, sample_rate) 
    plot_frequency_domain(signal, sample_rate)   
    play_sound(signal, sample_rate, device_index=11)


if __name__ == "__main__":
    main()