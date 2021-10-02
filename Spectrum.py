import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

# defining the wave
x = np.arange(0, 1, 0.001)
y1 = 2 * np.sin((x * 20*np.pi) + (np.pi/6))
y2 = 3 * np.sin((x * 100*np.pi)+ (np.pi/3))
y = y1 + y2
# plt.plot(y)

def amplitude_spectrum(data):
    #Extract amplitudes of frequency components (amplitude spectrum)==========
    data_points = np.size(data)
    length = np.size(data)
    # computind fourier transform---------------------------------------------
    fourier_transformed = scipy.fft.fft(data)
    #computing sample frequencies---------------------------------------------
    freq = np.fft.fftfreq(data_points, d=length/2) 
    #scaling frequencies
    freq = (freq * data_points) / 2 
    #computing amplitudes-----------------------------------------------------
    amplitude = np.abs(fourier_transformed) 
    #scaling amplitudes
    amplitude = (amplitude * 2) / data_points 
    #sorting indexes
    amplitude = np.reshape(amplitude, (np.shape(amplitude)[0], 1))
    freq = freq.reshape(np.shape(freq)[0],1)
    fp = np.concatenate((freq, amplitude), axis = 1)
    fp = fp[np.argsort(fp[:,0])]
    amplitude = fp[:,1]
    freq = fp[:,0]
    return amplitude, freq

def phase_spectrum(data, ignore, tr_order):
    # Extract phases of frequency components (phase spectrum)=================
    data_points = np.size(data)
    length = np.size(data)
    # computind fourier transform---------------------------------------------
    fourier_transformed = scipy.fft.fft(data)
    #computing sample frequencies---------------------------------------------
    freq = np.fft.fftfreq(data_points, d=length/2)
    #scaling frequencies
    freq = (freq * data_points) / 2
    #detect noise (very small numbers (eps)) and ignore them------------------
    # #tolerance threshold
    if ignore == True:
        threshold = np.max(np.abs(fourier_transformed)) / tr_order
        #maskout values that are below the threshold
        fourier_transformed[np.abs(fourier_transformed) < threshold] = 0 
    #seperate real and imaginary parts of fft---------------------------------
    real = fourier_transformed.real
    imaginary = fourier_transformed.imag
    phase = np.arctan2(imaginary,real)
    #sorting indexes
    phase = np.reshape(phase, (np.shape(phase)[0],1))
    freq = freq.reshape(np.shape(freq)[0],1)
    fp = np.concatenate((freq, phase), axis = 1)
    fp = fp[np.argsort(fp[:, 0])]
    phase = fp[:,1]
    freq = fp[:,0]
    return phase, freq

def ft_reconstruct(frequencies, amplitudes, phases):
    len_sample = np.size(frequencies)
    t = 0
    reconstruct = []
    while t < len_sample:
        b = []
        j = 0
        while j < len_sample:
            a = amplitudes[j] * np.cos(2*np.pi * frequencies[j] * t + (phases[j]))
            b.append(a)
            j = j + 1
        reconstruct.append(np.sum(b))
        t = t + 1
    reconstruct = np.asarray(reconstruct)
    reconstruct = (reconstruct/2)
    return reconstruct

#-----------------------------------------------------------------------------
# Spectrum extraction
amplitudes, frequencies = amplitude_spectrum(y)
phases, frequencies = phase_spectrum(y, True)

# plot
fig,a =  plt.subplots(2,sharex=True)
a[0].plot(frequencies, amplitudes)
a[1].plot(frequencies, phases)
a[0].set_xlabel("Frequency")
a[0].set_ylabel("Amplitude")
a[1].set_xlabel("Frequency")
a[1].set_ylabel("Phase")

# # Reconstruction
# reconstruct = ft_reconstruct(frequencies, amplitudes, phases)
# plt.plot(y)
# plt.plot(reconstruct)
