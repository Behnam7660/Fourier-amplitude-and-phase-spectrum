# Fourier-amplitude-and-phase-spectrum
This code calculates amlitude and phase spectrum of a given 1D curve usind fft algorithem.
It is consist of three functions: 

1 - amplitude_spectrum(data) : 

    data = 1D array representing a wave.
    return = amplitudes, frequencies.
    
2 - phase_spectrum(data, ignore, tr_order) : 

    data = 1D array representing a wave.
    ignore = boolean type, pute true to maskout values that are below the threshold.
    tr_order = threshold order, 10000 would be apt.
    return = phases, frequencies.
    
3 - ft_reconstruct(frequencies, amplitudes, phases) :

    frequencies = sequence of frequencies.
    amplitudes = sequence of amplitudes.
    phases = sequence of phases.
    return = reconstructed wave.
    
The first two functions calculate amplitude and phase spectrum. The third function reconstructs the wave using frequencies, amplitudes, and phases that can be obtained from functions 1 and 2. Reconstruction procedure follows the wave function:

    wave = SUM(amplitudes[j] * cos(2*pi * frequencies[j] * t + (phases[j]))

Here is an example of a wave which composed of two simple sine waves:

    y1 = 2 * sin((x * 20*pi) + (pi/6))  ;  amp = 2, freq = 20*pi, phase = pi/6
    y2 = 3 * sin((x * 100*pi)+ (pi/3))  ;  amp = 3, freq = 100*pi, phase = pi/3
    y = y1 + y2

![Figure_1](https://user-images.githubusercontent.com/72737338/135691327-e46a9077-b852-4576-8eaf-845d20c65c99.png)

Related amplitude and phase spectrum:

![Figure_2](https://user-images.githubusercontent.com/72737338/135691334-7d46f24d-085c-465f-9a1d-2ec16d238e43.png)
