import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

from scipy.fftpack import fft
from scipy.io import wavfile

song = wavfile.read('1-05_Let_It_Go.wav')

a = song[1] # this is a two channel soundtrack, I get the first track
one = a[:,0]
two = a[:,1]


print one
print two

b=[(ele/2**16.)*2-1 for ele in one] # this is 8-bit track, b is now normalized on [-1,1)
twob=[(ele/2**16.)*2-1 for ele in two]

c = fft(b) # calculate fourier transform (complex numbers list)
twoc = fft(twob)

d = len(c)/2  # you only need half of the fft list (real signal symmetry)
twod = len(twoc)/2


plt.plot(abs(c[:(d-1)]),'r')
#plt.axis([0, 100000, 0, 2000])
plt.show()

plt2.plot(abs(c[:(d-1)]),'r')
#plt2.axis([0, 100000, 0, 2000])
plt2.show()
