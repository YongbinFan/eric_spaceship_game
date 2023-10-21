import pygame
import os

# Set the constant variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60
BATTLESHIP_WIDTH, BATTLESHIP_HEIGHT = 55, 40
VEL = 5
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
BLACK = (0, 0, 0)
BULLET_VEL = 7

# Make the Battleships
YELLOW_BATTLESHIP_IMG = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_BATTLESHIP = pygame.transform.scale(YELLOW_BATTLESHIP_IMG, (BATTLESHIP_WIDTH, BATTLESHIP_HEIGHT))
YELLOW_BATTLESHIP = pygame.transform.rotate(YELLOW_BATTLESHIP, 90)
RED_BATTLESHIP_IMG = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_BATTLESHIP = pygame.transform.scale(RED_BATTLESHIP_IMG, (BATTLESHIP_WIDTH, BATTLESHIP_HEIGHT))
RED_BATTLESHIP = pygame.transform.rotate(RED_BATTLESHIP, 270)

# Change the title
pygame.display.set_caption("EriX Game!!!")


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_BATTLESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_BATTLESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_move(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:  # YELLOW-LEFT
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # YELLOW-RIGHT
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0:  # YELLOW-UP
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:  # YELLOW-DOWN
        yellow.y += VEL


def red_move(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # RED-LEFT
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RED-RIGHT
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0:  # RED-UP
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:  # RED-DOWN
        red.y += VEL


def main():
    red = pygame.Rect(700, 300, BATTLESHIP_WIDTH, BATTLESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, BATTLESHIP_WIDTH, BATTLESHIP_HEIGHT)
    run = True
    clock = pygame.time.Clock()
    red_bullets = []
    yellow_bullets = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(yellow.x, + yellow.width, yellow.y + yellow.height / 2 - 2)
                    yellow_bullets.append(bullet)

        key_pressed = pygame.key.get_pressed()
        yellow_move(key_pressed, yellow)
        red_move(key_pressed, red)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
