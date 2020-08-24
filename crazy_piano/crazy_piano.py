import pandas as pd

def compute_frequencies(m=12, f0=440, base=2, low_thresh=20, high_thresh=8000):
    '''
    PURPOSE:
    Generates a set of frequencies corresponding to different numbers of notes per octave. 
    
    Frequency determination formula link: https://pages.mtu.edu/~suits/NoteFreqCalcs.html
    fn = f0 * (a)^n, where...

    INPUT VALUES:
        m: The number of steps in an octave. 12 is standard.
        f0: Baseline frequency. 440 Hz is conventional starting point for A4 pitch.
        base: The base of growth for frequencies. Determines how fast the frequencies increase.
        low_thresh: The lowest frequency allowed. 20 Hz is low limit of human hearing.
        high_thresh: The highest frequency allowed. 8000 Hz traditionally the 8th octave.
    
    COMPUTED VALUES:
    n: Number of half steps away from the fixed note. Higher note = (+), lower = (-)
    fn: Trequency of the note n half steps away.
    a: (base)^(1/m) = the mth root of the base.
    '''
    
    n, octave, note_number = 0, 0, 0
    a = base**(1/m)
    fn = f0
    freq_list = []
    
    while fn < high_thresh:    
        for note_number in range(m):
            fn = f0 * a**n
            freq_list.append([octave, note_number, fn])
            n += 1
        octave += 1
    
    n, octave, note_number = 0, 0, 0
    while fn > low_thresh:
        octave -= 1
        for note_number in range(m-1, -1, -1):
            n -= 1                
            fn = f0 * a**n
            freq_list.append([octave, note_number, fn])
    
    freq_df = pd.DataFrame(freq_list, columns=['Octave', 'Note Number', 'Frequency (Hz)']).sort_values(by = ['Octave', 'Note Number'])
    return freq_df
