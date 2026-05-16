# PRNG Algorithm Lab

## Summary

This project explores and compares pseudorandom number generator (PRNG) algorithms.
We implemented eight PRNGs from scratch in Python: Linear Congruential Generator, Xorshift,
Mersenne Twister, PCG, Lagged Fibonacci, Blum Blum Shub, SHA-256, and Middle Square.
Each algorithm uses a different mathematical approach to generate sequences of numbers that appear random.

We built an interactive GUI using pygame that lets users select any generator, generate a
sequence of numbers, and view the results as a bar chart alongside the raw values on screen.

## Algorithms

| Algorithm | Description |
|---|---|
| Linear Congruential Generator | Classic formula: x = (a*x + c) % m |
| Xorshift | Uses XOR and bit shift operations |
| Mersenne Twister | Based on a 624-element state array with period 2^19937 - 1 |
| PCG | Permuted Congruential Generator, improved LCG variant |
| Lagged Fibonacci | Combines two earlier values in a buffer using addition |
| Blum Blum Shub | Cryptographically motivated, based on quadratic residues |
| SHA-256 | Uses a cryptographic hash function as a number source |
| Middle Square | Von Neumann's original method; squares the seed and extracts middle digits |

## Technologies

- Python
- pygame
