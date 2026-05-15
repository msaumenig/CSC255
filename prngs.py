import math
import time 
import pygame

def mersennetwister(seed, n):
    mt = [0] * 624
    mt[0] = seed
    for i in range(1, 624):
        mt[i] = (1812433253 * (mt[i-1] ^ (mt[i-1] >> 30)) + i) & 0xFFFFFFFF
 
    index = 624
    results = []
 
    for _ in range(n):
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
    for _ in range(n):
        x = (a * x + c) % m
        results.append(x)
    return results
 
 
def xorshift(seed, n):
    results = []
    x = seed
    for _ in range(n):
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        x &= 0xFFFFFFFF
        results.append(x)
    return results



import time

def menu():
    while True:
        print("\n==============================")
        print("   RANDOM NUMBER GENERATORS")
        print("==============================")
        print("1. Mersenne Twister")
        print("2. LCG")
        print("3. Xorshift")
        print("4. Exit")
        print("==============================")

        choice = input("Choose generator: ")

        if choice == "4":
            print("Goodbye!")
            break

        try:
            n = int(input("How many numbers? "))
            use_time = input("Use current time as seed? (y/n): ").lower()

            if use_time == "y":
                seed = time.time_ns() & 0xFFFFFFFF
            else:
                seed = int(input("Enter seed: "))

            if choice == "1":
                numbers = mersennetwister(seed, n)
                name = "Mersenne Twister"
            elif choice == "2":
                numbers = lcg(seed, n)
                name = "LCG"
            elif choice == "3":
                if seed == 0:
                    print("Xorshift seed cannot be 0.")
                    continue
                numbers = xorshift(seed, n)
                name = "Xorshift"
            else:
                print("Invalid choice.")
                continue

            print(f"\n{name} results")
            print(f"Seed: {seed}")
            print("------------------------------")

            for i, num in enumerate(numbers, start=1):
                print(f"{i}: {num}")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    menu()