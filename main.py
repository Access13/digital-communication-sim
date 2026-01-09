from config import NUM_BITS, AMPLITUDE, BIT_RATE, SNR_DB
from source.bit_generator import generate_bits
from modulation.ask import ask_modulate
from channel.awgn import awgn
from demodulation.ask_demod import ask_demodulate
from analysis.ber import ber
from visualisation.plots import plot_signals  

# 1. Generate bits
bits = generate_bits(NUM_BITS)
print("Original bits:", bits[:20], "...")

# 2. Modulate
tx_signal = ask_modulate(bits, AMPLITUDE, BIT_RATE)
print("Transmitted signal length:", len(tx_signal))

# 3. Pass through AWGN channel
rx_signal = awgn(tx_signal, SNR_DB)

# 4. Demodulate
received_bits = ask_demodulate(rx_signal, NUM_BITS, BIT_RATE)

# 5. Calculate BER
error_rate = ber(bits, received_bits)
print("BER:", error_rate)

# 6. Plot signals
plot_signals(tx_signal, rx_signal, bits, received_bits, BIT_RATE, fs=10000, num_bits_to_plot=10)
