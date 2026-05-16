"""
CSC 255
Group Programming Assignment
Group 4
5/15/2026

A driver file that launches a Pygame application to demonstrate various PRNG algorithms.
"""
from prngs import *
import pygame

def pygame_gui():
    """Launches a simple Pygame app to demonstrate various PRNG algorithms."""
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