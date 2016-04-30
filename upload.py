import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile

song = wavfile.read('t1.wav')

a = song[1] # this is a two channel soundtrack, I get the first track

print a
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = len(c)/2  # you only need half of the fft list (real signal symmetry)

plt.plot(abs(c[:(d-1)]),'r')
plt.show()
