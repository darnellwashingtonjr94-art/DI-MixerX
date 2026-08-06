# DI-MixerX

**DI-MixerX** (Device Identifier Mixer) is a honeypot data generator designed to randomly change and spoof hardware and network information. 

The goal of this project is to leave malicious actors lost and confused by feeding them dynamically generated, completely fake device identifiers. It acts as a trap, serving up fake "confidential" data to waste attackers' time and resources.

## Features
* Generates randomized IP addresses (IPv4/IPv6).
* Spoofs Wi-Fi and Bluetooth MAC addresses.
* Simulates randomized device uptimes.
* Generates realistic, but fake, Android build numbers.

## Usage
Run the main script to generate a fresh batch of fake device identifiers:
```bash
python mixer.py
