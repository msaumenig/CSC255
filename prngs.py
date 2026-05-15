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



def pygame_gui():
    pygame.init()

    WIDTH, HEIGHT = 900, 650
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PRNG Visual Generator")

    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 36, bold=True)
    font = pygame.font.SysFont("arial", 24)
    small_font = pygame.font.SysFont("arial", 20)

    selected = "LCG"
    seed = time.time_ns() & 0xFFFFFFFF
    count = 6
    results = []
    loading = False

    bg = (24, 26, 32)
    card = (38, 42, 52)
    button = (65, 72, 90)
    button_active = (88, 101, 242)
    text = (235, 235, 235)
    muted = (160, 165, 180)
    border = (80, 85, 100)

    buttons = {
        "Mersenne Twister": pygame.Rect(40, 120, 230, 50),
        "LCG": pygame.Rect(290, 120, 120, 50),
        "Xorshift": pygame.Rect(430, 120, 150, 50),
        "Generate": pygame.Rect(650, 120, 190, 50),
    }

    def draw_text(value, x, y, font_obj=font, color=text):
        img = font_obj.render(str(value), True, color)
        screen.blit(img, (x, y))

    def draw_button(label, rect, active=False):
        color = button_active if active else button
        pygame.draw.rect(screen, color, rect, border_radius=12)
        pygame.draw.rect(screen, border, rect, 2, border_radius=12)

        img = small_font.render(label, True, text)
        screen.blit(
            img,
            (
                rect.centerx - img.get_width() // 2,
                rect.centery - img.get_height() // 2,
            ),
        )

    def generate_numbers():
        current_seed = time.time_ns() & 0xFFFFFFFF

        if selected == "Mersenne Twister":
            nums = mersennetwister(current_seed, count)
        elif selected == "LCG":
            nums = lcg(current_seed, count)
        else:
            if current_seed == 0:
                current_seed = 1
            nums = xorshift(current_seed, count)

        return current_seed, nums

    running = True

    while running:
        screen.fill(bg)

        draw_text("Pseudo-Random Number Generator", 40, 35, title_font)
        draw_text("Choose an algorithm and generate numbers.", 40, 80, small_font, muted)

        for label, rect in buttons.items():
            is_active = label == selected
            draw_button(label, rect, is_active)

        pygame.draw.rect(screen, card, (40, 210, 800, 390), border_radius=18)

        draw_text(f"Algorithm: {selected}", 70, 240)
        draw_text(f"Seed: {seed}", 70, 275, small_font, muted)
        draw_text(f"Count: {count}", 70, 305, small_font, muted)

        if loading:
            draw_text("Generating numbers...", 70, 360, font)
            pygame.draw.circle(screen, button_active, (360, 370), 10)
        else:
            draw_text("Results", 70, 350, font)

            y = 390
            for i, number in enumerate(results[:12], start=1):
                draw_text(f"{i:02}. {number}", 80, y, small_font)
                y += 25

            if not results:
                draw_text("No numbers generated yet.", 80, 390, small_font, muted)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos

                if buttons["Mersenne Twister"].collidepoint(mouse):
                    selected = "Mersenne Twister"

                elif buttons["LCG"].collidepoint(mouse):
                    selected = "LCG"

                elif buttons["Xorshift"].collidepoint(mouse):
                    selected = "Xorshift"

                elif buttons["Generate"].collidepoint(mouse):
                    loading = True
                    pygame.display.flip()

                    pygame.time.delay(300)

                    seed, results = generate_numbers()
                    loading = False

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    pygame_gui()