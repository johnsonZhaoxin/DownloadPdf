import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
# 如果源文件不是16bit，可以用sox input.wav -r 16 -b 44.1k output.wav转一下。terminal终端中操作
sampFreq, sound = wavfile.read('smf27Analysis.wav')
sound = sound / 2.0**15
#print(sound.shape)

length_in_s = sound.shape[0] / sampFreq
# print(length_in_s) #5s的音频
# plt.subplot(2,1,1)
# plt.plot(sound, 'r')
# plt.xlabel("frequency")
# plt.show()

time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
plt.subplot(2,1,1)
plt.plot(time, sound[:], 'r')
plt.xlabel("time, s")
plt.show() #这是全部的d-t图

signal = sound[:]
plt.plot(time[6000:7000], signal[6000:7000])
plt.xlabel("time, s")
plt.ylabel("Signal, relative units")
plt.show() #这是部分放大的时候图像


# 傅里叶变换，分析频率
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)

plt.plot(freq, fft_spectrum_abs)
plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.show()

for i,f in enumerate(fft_spectrum_abs):
    if f > 350: #滤掉噪音
        print('frequency = {} Hz with amplitude {} '.format(np.round(freq[i],1),  np.round(f)))

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
sampFreq, sound = wavfile.read('smf27Analysis.wav')
sound = sound / 2.0**15
#print(sound.shape)

length_in_s = sound.shape[0] / sampFreq
# print(length_in_s) #5s的音频
# plt.subplot(2,1,1)
# plt.plot(sound, 'r')
# plt.xlabel("frequency")
# plt.show()

time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
plt.subplot(2,1,1)
plt.plot(time, sound[:], 'r')
plt.xlabel("time, s")
plt.show() #这是全部的d-t图

signal = sound[:]
plt.plot(time[6000:7000], signal[6000:7000])
plt.xlabel("time, s")
plt.ylabel("Signal, relative units")
plt.show() #这是部分放大的时候图像


# 傅里叶变换，分析频率
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)

plt.plot(freq, fft_spectrum_abs)
plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.show()

for i,f in enumerate(fft_spectrum_abs):
    if f > 350: #滤掉噪音
        print('frequency = {} Hz with amplitude {} '.format(np.round(freq[i],1),  np.round(f)))

