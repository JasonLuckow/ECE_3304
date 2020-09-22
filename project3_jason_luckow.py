"""
Python Project 3
Author: Jason Luckow
Date: 9/20/2020
Song: Bohemian Rhapsody
"""
import numpy as np
import simpleaudio as sa
import time


def add(freq1, freq2, freq3, duration, delay):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    note1 = np.sin(freq1 * t * 2 * np.pi)
    note2 = np.sin(freq2 * t * 2 * np.pi)
    note3 = np.sin(freq3 * t * 2 * np.pi)
    audio = np.zeros((delay, 2))

    n = len(t)
    audio[0: n, 0] += note1
    audio[0: n, 1] += note1
    audio[0: n, 0] += note2
    audio[0: n, 1] += note2
    audio[0: n, 0] += note3
    audio[0: n, 1] += note3

    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 2, 2, sample_rate)
    play_obj.wait_done()


# notes
Gnat1 = 48.999

Dsh2 = 77.782
Gnat2 = 97.999
Ash2 = 116.541

Dnat3 = 146.832
Fnat3 = 174.614
Gnat3 = 195.998
Gsh4 = 415.305
Anat3 = 220
Ash3 = 233.082

Cnat4 = 261.626
Dnat4 = 293.665
Dsh4 = 311.127
Enat4 = 329.628
Fnat4 = 349.228
Gnat4 = 391.995
Anat4 = 440
Ash4 = 466.164

Cnat5 = 523.251
Dsh5 = 622.254

Cnat6 = 1046.502
Anat6 = 1760

print("Song: Bohemian Rhapsody")

# measure 1
add(Dnat4, Fnat4, 0, .48, 21168)
add(Dnat4, Fnat4, 0, .48, 21168)
add(Dnat4, Fnat4, 0, .48, 21168)
add(Dnat4, Fnat4, 0, .65, 35000)
add(Dnat4, Fnat4, 0, .90, 44000)

time.sleep(.4)

# measure 2
add(Cnat4, Enat4, Gnat4, .48, 21168)
add(Cnat4, Enat4, Gnat4, .48, 21168)
add(Cnat4, Enat4, Fnat4, .48, 21168)
add(Cnat4, Enat4, Gnat4, .48, 21168)
add(Cnat4, Enat4, Gnat4, .48, 21168)
add(Ash3, Enat4, Gnat4, .92, 42000)

time.sleep(.4)

# measure 3
add(Cnat4, Fnat4, Anat4, .48, 21168)
add(Cnat4, Fnat4, Anat4, .48, 21168)
add(Cnat4, Fnat4, Anat4, .48, 21168)
add(Cnat4, Fnat4, Ash4, .49, 22000)
add(Cnat4, Fnat4, Anat4, .99, 44000)

add(Fnat3, 0, 0, .45, 21000)
add(Fnat3, 0, 0, .45, 21000)

# measure 4
add(Dnat4, Fnat4, Ash4, .46, 20300)
add(Dnat4, Fnat4, Ash4, .46, 20300)
add(Cnat4, Gnat4, Ash4, .46, 20300)
add(Dnat4, Fnat4, Ash4, .46, 20300)
add(Anat3, Dsh4, Anat4, .46, 20300)
add(Fnat3, Dnat4, Fnat4, .96, 47000)

time.sleep(.6)

# measure 5
add(Gnat1, Gnat2, Gnat3, 1, 44200)
add(Ash3, Gnat1, Gnat3, .55, 25000)
add(Dnat4, Gnat1, Gnat3, .55, 25000)
add(Gnat4, Gnat1, Gnat3, .55, 25000)
add(Dnat4, Gnat1, Gnat3, .55, 25000)
add(Ash3, Gnat1, Gnat3, .55, 25000)
add(Gnat3, Gnat1, Gnat3, .40, 35000)
add(Ash2, Dnat3, Ash3, 2.5, 111000)

time.sleep(.65)

# measure 6
add(Dsh2, Gnat4, Ash4, .45, 25000)
add(Dsh2, Dsh4, Gnat4, .45, 25000)
add(Dsh2, Gnat4, Ash4, .45, 25000)
add(Dsh2, Ash4, Ash4, .35, 20000)
add(Dsh2, Gsh4, Cnat5, .35, 20000)
add(Dsh2, Dnat4, Dsh5, .35, 17000)
add(Dsh2, Dnat4, Dsh5, .1, 15000)



