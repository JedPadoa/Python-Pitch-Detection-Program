from __future__ import division
import numpy as np
from scipy import signal
from Parabolic import parabolic
from numpy.fft import rfft
from pylab import plot, log, copy




def freq_from_fft(sig, fs):
    """
    Estimate frequency from peak of FFT
    """
    # Compute Fourier transform of windowed signal
    windowed = sig * signal.blackmanharris(len(sig))
    f = np.fft.fft(windowed)

    # Find the peak and interpolate to get a more accurate peak
    i = np.argmax(abs(f))

    i_interp = parabolic(log(abs(f)), i)[0]

    # Convert to equivalent frequency
    return fs * i_interp / len(windowed)

def freq_from_HPS(sig, fs):
    """
    Estimate frequency using harmonic product spectrum (HPS)
    """
    windowed = sig * signal.blackmanharris(len(sig))

    # harmonic product spectrum:
    c = abs(rfft(windowed))
    maxharms = 6
    plot(log(c))
    arr = np.zeros(maxharms)
    for x in range(2, maxharms):
        a = copy(c[::x])  # Should average or maximum instead of decimating
        #max(c[::x],c[1::x],c[2::x],...)
        c = c[:len(a)]
        i = np.argmax(abs(c))
        true_i = parabolic(abs(c), i)[0]
        arr[x] = fs * true_i / len(windowed)
        c *= a
    return arr[3]


def freq_from_HPS2(sig, fs):

    windowed = sig * signal.blackmanharris(len(sig))

    c = abs(rfft(windowed))

    i = np.argmax(abs(c))
    true_i = parabolic(abs(c), i)[0]

    freq = fs * true_i / len(windowed)

    return freq



