# visualisation/plots.py
import matplotlib.pyplot as plt

def plot_signals(tx_signal, rx_signal, bits, received_bits, bit_rate, fs=10000, num_bits_to_plot=10):
    """
    Plots a portion of the transmitted and received ASK signals and compares bits.
    
    Parameters:
    - tx_signal: transmitted ASK signal (numpy array)
    - rx_signal: received noisy signal (numpy array)
    - bits: original bit array
    - received_bits: demodulated bit array
    - bit_rate: number of bits per second
    - fs: sampling frequency in Hz
    - num_bits_to_plot: how many bits to show
    """
    T = 1 / bit_rate
    samples_per_bit = int(T * fs)
    N = num_bits_to_plot * samples_per_bit

    t = [i/fs for i in range(N)]

    plt.figure(figsize=(12, 6))

    # Transmitted vs received signals
    plt.subplot(2, 1, 1)
    plt.plot(t, tx_signal[:N], label="Transmitted Signal")
    plt.plot(t, rx_signal[:N], label="Received Signal", alpha=0.7)
    plt.title("ASK Transmitted vs Received Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    # Original vs received bits
    plt.subplot(2, 1, 2)
    plt.stem(bits[:num_bits_to_plot], linefmt='g', markerfmt='go', basefmt='k-', label='Original Bits')
    plt.stem(received_bits[:num_bits_to_plot], linefmt='r', markerfmt='ro', basefmt='k-', label='Received Bits')
    plt.title("Original vs Received Bits")
    plt.xlabel("Bit Index")
    plt.ylabel("Bit Value")
    plt.legend()

    plt.tight_layout()
    plt.show()
