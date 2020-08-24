
crazy-piano
===========
Assists in the exploration of how we **define** music. Currently generates a set of frequencies for any number of notes in an octave. 10-keys-per-octave keyboard? Why not!

Installation (with pip)
-----------------------
`pip install crazy-piano`

Functionality
==============

List of Functions
-------------------------------------------------
 - **compute_frequencies(m=12, f0=440, base=2, low_thresh=20, high_thresh=8000)**: Generates a set of frequencies corresponding to different numbers of notes per octave. Based on a modified version of the [formula for computing frequencies in an octave.](https://pages.mtu.edu/~suits/NoteFreqCalcs.html) 
	 -  m: The number of steps in an octave. 12 is standard.
	 - f0: Baseline frequency. 440 Hz is conventional starting point for A4 pitch.
	 - base: The base of growth for frequencies. Determines how fast the frequencies increase.
	 - low_thresh: The lowest frequency allowed. 20 Hz is low limit of human hearing.
		 - When `low_thresh` is met, still finishes the octave. i.e. If the 3rd note of an octave is below `low_thresh`, will still return the 1st and 2nd notes of that octave.
	 - high_thresh: The highest frequency allowed. 8000 Hz traditionally the 8th octave.
		 - When `high_thresh` is met, still finishes the octave. i.e. If the `m-2` note of an octave is above `high_thresh` , will still return the `m-1` and `m` notes of that octave.

*Ideas for more? Create an issue, or email mikealtonji@gmail.com with feedback.*

Usage
-------------------------------------------------
Creates a pandas dataframe containing the frequencies for each note, where 440 Hz is the base value. Uses default values for low and high frequency cut-offs.
```
from crazy_piano import compute_frequencies
keyboard_10_notes = compute_frequencies(m=10)
```
Output Dataframe Columns
-------------------------------------------------

Octave: `f0` is the reference point. It is the 0th note of the 0th octave. `Octave`s lower are negative, and larger are positive. Integer.
Note Number: `f0` is the reference point. It is the 0th note of any octave. The largest `Note Number` is therefore `m-1`. Integer.
Frequency (Hz): The frequency corresponding to the `Octave` and `Note Number`, in Hertz. Float.

Contributors
============
* Michael Altonji
*Interested in collaborating? Email mikealtonji@gmail.com, or submit issues for features you'd like to see in the future!*

License
=======
[MIT License](https://opensource.org/licenses/MIT)
