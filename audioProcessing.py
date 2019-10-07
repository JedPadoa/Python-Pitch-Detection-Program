import numpy as np
from numpy import arange
from pitchDetection import freq_from_HPS2
from scipy.signal import find_peaks
from peakDetect import findThresh

#creates an array of frequencies found within incremental steps of 1000 signal frames

def freqArray(s1, sampFreq):
    num = int(len(s1)/130)
    array = arange(0, len(s1), 5000)
    detected_freqs = np.zeros(len(array)).tolist()

    for i in range(0, len(array), 1):
        if i < len(array) - 1:
            detected_freqs[i] = freq_from_HPS2(s1[array[i]:array[i+1]], sampFreq)
        elif i == len(array) - 1:
            detected_freqs[i] = freq_from_HPS2(s1[array[i]:len(s1)], sampFreq)

    return detected_freqs

#removes frequency values that correspond to the same note as others

def removeUnnecessary(freqs):
    newArr = []
    i = 0
    counter = 0
    j = 0
    for i in range(0, len(freqs) - 1):
        if abs(freqs[i+1] - freqs[i]) < 15:
            counter += freqs[i+1]
            j += 1
            print(j, counter)
        else:
            if j != 0:
                average = counter / (j)
                newArr.append(average)
                counter = 0
                j = 0

    return newArr


