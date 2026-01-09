# demodulation/ask_demod.py
import numpy as np

def ask_demodulate(received_signal, num_bits, bit_rate, fs=10000):
    """Simple ASK demodulator using envelope detection"""
    T = 1 / bit_rate
    samples_per_bit = int(T * fs)
    bits = []

    for i in range(num_bits):
        sample = received_signal[i*samples_per_bit:(i+1)*samples_per_bit]
        avg = np.mean(np.abs(sample))
        bits.append(1 if avg > 0.5 else 0)

    return np.array(bits)
