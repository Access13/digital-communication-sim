# source/bit_generator.py
import numpy as np

def generate_bits(num_bits):
    """Generate a random sequence of 0s and 1s."""
    return np.random.randint(0, 2, num_bits)
