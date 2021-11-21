import pygame
import sys


def main():
    # General Setup
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Castle Wars')

    # Global variables
    bg_color = pygame.Color('#2F373F')
    accent_color = (27, 35, 43)
    middle_strip = pygame.Rect(screen_width / 2 - 2, 0, 4, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Background Stuff
        screen.fill(bg_color)
        pygame.draw.rect(screen, accent_color, middle_strip)

        # Rendering
        pygame.display.flip()
        clock.tick(120)


if __name__ == "__main__":
    main()
