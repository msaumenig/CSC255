"""
CSC 255
Group Programming Assignment
Group 4
5/15/2026

A module that contains multiple pseudorandom number generator (PRNG) algorithms.
"""
import pygame
import time
import math
import hashlib


# PRNG ALGORITHMS

def lcg(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using a Linear Congruential Generator (LCG)."""
    a, c, m = 1664525, 1013904223, 2**32
    x = seed
    out = []
    for _ in range(n):
        x = (a * x + c) % m
        out.append(x)
    return out


def xorshift(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using a Xorshift algorithm."""
    x = seed or 1
    out = []
    for _ in range(n):
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        x &= 0xFFFFFFFF
        out.append(x)
    return out


def pcg(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using a Permuted Congruential Generator (PCG)."""
    x = seed
    out = []
    for _ in range(n):
        x = (x * 747796405 + 2891336453) & 0xFFFFFFFF
        v = x ^ (x >> ((x >> 28) + 4))
        v = (v * 277803737) & 0xFFFFFFFF
        v ^= v >> 22
        out.append(v & 0xFFFFFFFF)
    return out


def lagged_fibonacci(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using a Lagged Fibonacci Generator (LFG/LFib)."""
    buf = [(seed + i * 99991) & 0xFFFFFFFF for i in range(55)]
    out = []
    for i in range(n):
        x = (buf[(i - 24) % 55] + buf[(i - 55) % 55]) & 0xFFFFFFFF
        buf.append(x)
        out.append(x)
    return out


def blum_blum_shub(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using the Blum Blum Shub (BBS) method."""
    # small demo version (not secure parameters)
    p, q = 383, 503
    m = p * q
    x = (seed % m) or 3
    out = []
    for _ in range(n):
        x = (x * x) % m
        out.append(x)
    return out


def sha256_prng(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using SHA-256."""
    out = []
    x = str(seed).encode()
    for _ in range(n):
        x = hashlib.sha256(x).digest()
        out.append(int.from_bytes(x[:4], "big"))
    return out


def middle_square(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using the middle-square method."""
    x = seed
    out = []
    for _ in range(n):
        s = str(x * x).zfill(16)
        mid = len(s) // 2
        x = int(s[mid-2:mid+2]) if len(s) >= 4 else int(s)
        out.append(x)
    return out


def mersenne_like(seed: int, n: int) -> list[int]:
    """Generates a list of n pseudorandom integers using a Mersenne Twister-like algorithm."""
    mt = [0] * 624
    mt[0] = seed
    for i in range(1, 624):
        mt[i] = (1812433253 * (mt[i-1] ^ (mt[i-1] >> 30)) + i) & 0xFFFFFFFF

    index = 624
    out = []

    for _ in range(n):
        if index >= 624:
            for i in range(624):
                y = (mt[i] & 0x80000000) + (mt[(i+1) % 624] & 0x7FFFFFFF)
                mt[i] = mt[(i + 397) % 624] ^ (y >> 1)
                if y % 2:
                    mt[i] ^= 2567483615
            index = 0

        y = mt[index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18
        index += 1
        out.append(y & 0xFFFFFFFF)

    return out

