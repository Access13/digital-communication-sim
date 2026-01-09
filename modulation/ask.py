# modulation/ask.py
import numpy as np

def ask_modulate(bits, amplitude, bit_rate, fs=10000):
    """
    Amplitude Shift Keying (ASK) modulation
    bits: array of 0s and 1s
    amplitude: signal amplitude
    bit_rate: bits per second
    fs: sampling frequency
    """
    T = 1 / bit_rate
    t = np.arange(0, T, 1/fs)
    signal = np.array([])

    for bit in bits:
        s = amplitude * bit * np.sin(2 * np.pi * 1000 * t)  # 1 kHz carrier
        signal = np.concatenate((signal, s))

    return signal
