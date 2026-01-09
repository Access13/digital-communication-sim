# channel/awgn.py
import numpy as np

def awgn(signal, snr_db):
    """Additive White Gaussian Noise channel"""
    snr_linear = 10**(snr_db / 10)
    power_signal = np.mean(signal**2)
    noise_power = power_signal / snr_linear
    noise = np.sqrt(noise_power) * np.random.randn(len(signal))
    return signal + noise
