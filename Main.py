from scipy.io import wavfile
from pylab import*
from audioProcessing import freqArray, removeUnnecessary

# import signal

sampFreq, sound = wavfile.read(r'C:\Users\jeddo\Documents\Image-Line\Data\FL Studio\Projects\Audio_3.wav')
s1 = sound[:, 0]

# plot time domain of signal

timeArray = arange(0, len(s1), 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000
x = arange(0, len(s1), 1)
plot(x, abs(s1), color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
plt.show()

freqVals = [523.3,	554.4,	587.3,	622.3,	659.3,	698.5,	740.0,	784.0,
            830.6,	880.0,	932.3,	987.8]

notes = ['C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5, ''A5', '#A#5', 'B5']

Identified_Notes = []

freqs = freqArray(s1, sampFreq)
# temporary bounding of frequency array --- at some point need to figure out how to unbound
freqs = [x for x in freqs if x < 1100]
# remove redundant frequency vals

print(freqs)
print(removeUnnecessary(freqs))



