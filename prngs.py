import math

def mersennetwister(seed, n):
    mt = [0] * 624
    mt[0] = seed
    for i in range(1, 624):
        mt[i] = (1812433253 * (mt[i-1] ^ (mt[i-1] >> 30)) + i) & 0xFFFFFFFF
 
    index = 624
    results = []
 
    for  in range(n):
        if index >= 624:
            for i in range(624):
                y = (mt[i] & 0x80000000) + (mt[(i + 1) % 624] & 0x7FFFFFFF)
                mt[i] = mt[(i + 397) % 624] ^ (y >> 1)
                if y % 2 != 0:
                    mt[i] ^= 2567483615
            index = 0
 
        y = mt[index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18
        index += 1
        results.append(y & 0xFFFFFFFF)
 
    return results
 
 
def lcg(seed, n):
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    results = []
    x = seed
    for  in range(n):
        x = (a * x + c) % m
        results.append(x)
    return results
 
 
def xorshift(seed, n):
    results = []
    x = seed
    for  in range(n):
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        x &= 0xFFFFFFFF
        results.append(x)
    return results
