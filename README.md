# Digital Communication Simulator

A clean, educational Python-based simulator for basic **digital communication systems**.

This project demonstrates the full chain of a simple digital communication system:
- Random bit generation
- **ASK** (Amplitude Shift Keying) modulation
- Transmission through an **AWGN** (Additive White Gaussian Noise) channel
- Demodulation
- **BER** (Bit Error Rate) calculation & performance analysis
- Signal visualization at every major step

Perfect for students, self-learners, and anyone interested in understanding the fundamentals of digital communications.

## Features

- Configurable simulation parameters (SNR, number of bits, etc.)
- Classic binary ASK modulation/demodulation
- Realistic AWGN channel model
- Accurate BER calculation & comparison with theory
- Beautiful matplotlib visualizations of time-domain signals

## System Block Diagram

Here’s the classic block diagram of the digital communication system being simulated:

<grok-card data-id="5f9552" data-type="image_card"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="cfb4b9" data-type="image_card"  data-arg-size="LARGE" ></grok-card>


## ASK Modulation – How it looks

Amplitude Shift Keying: '1' → high amplitude, '0' → low/no amplitude

Here are typical ASK waveforms:

<grok-card data-id="edbed4" data-type="image_card"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="8318f1" data-type="image_card"  data-arg-size="LARGE" ></grok-card>


## Example Output – Signal Through Noisy Channel

Transmitted ASK signal → AWGN channel → Received noisy signal:

<grok-card data-id="ab6c80" data-type="image_card"  data-arg-size="LARGE" ></grok-card>


## Performance – BER vs SNR Curve

One of the most important plots in digital communications — how error rate behaves with increasing signal-to-noise ratio:

<grok-card data-id="6a001e" data-type="image_card"  data-arg-size="LARGE" ></grok-card>


Typical theoretical vs simulated comparison (ASK usually needs ~3 dB more SNR than BPSK for same BER):

<grok-card data-id="c1d1d7" data-type="image_card"  data-arg-size="LARGE" ></grok-card>


## Installation

```bash
git clone https://github.com/Access13/digital-communication-sim.git
cd digital-communication-sim

# (Recommended) Create virtual environment
python -m venv venv
source venv/bin/activate     # Linux/macOS
# or on Windows: venv\Scripts\activate

pip install -r requirements.txt
