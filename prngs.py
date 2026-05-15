import pygame
import time
import math
import hashlib


# PRNG ALGOS

def lcg(seed, n):
    a, c, m = 1664525, 1013904223, 2**32
    x = seed
    out = []
    for _ in range(n):
        x = (a * x + c) % m
        out.append(x)
    return out


def xorshift(seed, n):
    x = seed or 1
    out = []
    for _ in range(n):
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        x &= 0xFFFFFFFF
        out.append(x)
    return out


def pcg(seed, n):
    x = seed
    out = []
    for _ in range(n):
        x = (x * 747796405 + 2891336453) & 0xFFFFFFFF
        v = x ^ (x >> ((x >> 28) + 4))
        v = (v * 277803737) & 0xFFFFFFFF
        v ^= v >> 22
        out.append(v & 0xFFFFFFFF)
    return out


def lagged_fibonacci(seed, n):
    buf = [(seed + i * 99991) & 0xFFFFFFFF for i in range(55)]
    out = []
    for i in range(n):
        x = (buf[(i - 24) % 55] + buf[(i - 55) % 55]) & 0xFFFFFFFF
        buf.append(x)
        out.append(x)
    return out


def blum_blum_shub(seed, n):
    # small demo version (not secure parameters)
    p, q = 383, 503
    m = p * q
    x = (seed % m) or 3
    out = []
    for _ in range(n):
        x = (x * x) % m
        out.append(x)
    return out


def sha256_prng(seed, n):
    out = []
    x = str(seed).encode()
    for _ in range(n):
        x = hashlib.sha256(x).digest()
        out.append(int.from_bytes(x[:4], "big"))
    return out


def middle_square(seed, n):
    x = seed
    out = []
    for _ in range(n):
        s = str(x * x).zfill(16)
        mid = len(s) // 2
        x = int(s[mid-2:mid+2]) if len(s) >= 4 else int(s)
        out.append(x)
    return out


def mersenne_like(seed, n):
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


# GUI / APP


def pygame_gui():
    pygame.init()

    W, H = 1000, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Advanced PRNG Algorithm Lab")

    font = pygame.font.SysFont("arial", 24)
    big = pygame.font.SysFont("arial", 34, bold=True)
    small = pygame.font.SysFont("arial", 18)

    algorithms = {
        "LCG": lcg,
        "Xorshift": xorshift,
        "Mersenne": mersenne_like,
        "PCG": pcg,
        "Lagged Fib": lagged_fibonacci,
        "BBS": blum_blum_shub,
        "SHA256": sha256_prng,
        "Middle Square": middle_square
    }

    selected = "LCG"
    seed = int(time.time_ns()) & 0xFFFFFFFF
    count = 12
    results = []

    buttons = {}
    x = 40
    for name in algorithms:
        buttons[name] = pygame.Rect(x, 120, 110, 45)
        x += 120

    gen_button = pygame.Rect(800, 120, 150, 45)

    def draw_hist(values):
        if not values:
            return

        max_v = max(values)
        base_y = 630
        bar_w = W // len(values)

        for i, v in enumerate(values):
            h = int((v / max_v) * 150)
            pygame.draw.rect(screen, (80, 120, 255),
                             (i * bar_w, base_y - h, bar_w - 2, h))

    running = True
    while running:
        screen.fill((18, 18, 25))

        screen.blit(big.render("PRNG Algorithm Laboratory", True, (240, 240, 240)), (40, 30))

   
        for name, rect in buttons.items():
            color = (90, 100, 255) if name == selected else (60, 60, 80)
            pygame.draw.rect(screen, color, rect, border_radius=8)
            screen.blit(small.render(name, True, (255, 255, 255)), (rect.x + 8, rect.y + 12))

        pygame.draw.rect(screen, (0, 200, 140), gen_button, border_radius=8)
        screen.blit(small.render("GENERATE", True, (0, 0, 0)), (gen_button.x + 25, gen_button.y + 12))

        screen.blit(font.render(f"Algorithm: {selected}", True, (220, 220, 220)), (40, 200))
        screen.blit(font.render(f"Seed: {seed}", True, (180, 180, 180)), (40, 230))

        y = 270
        for i, v in enumerate(results[:10]):
            screen.blit(small.render(f"{i+1}. {v}", True, (200, 200, 200)), (40, y))
            y += 22

        draw_hist(results)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = e.pos

                for name, rect in buttons.items():
                    if rect.collidepoint(pos):
                        selected = name

                if gen_button.collidepoint(pos):
                    seed = int(time.time_ns()) & 0xFFFFFFFF
                    results = algorithms[selected](seed, count)

        pygame.time.Clock().tick(60)

    pygame.quit()


if __name__ == "__main__":
    pygame_gui()
