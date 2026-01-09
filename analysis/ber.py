# analysis/ber.py
import numpy as np

def ber(original_bits, received_bits):
    errors = np.sum(original_bits != received_bits)
    return errors / len(original_bits)
