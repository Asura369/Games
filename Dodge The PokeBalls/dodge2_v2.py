# imports
import pygame
import random

from pikachu import Pikachu
from pokeball import Pokeball


def collisions():
    for i in pokeballs:
        if i.collided(pikachu.rect):
            return True
    return False


def spawnPokeball():
    num = random.randint(1, 4)
    if num == 1:
        x = random.randint(0, screen_width - 30)
        y = 0
    elif num == 2:
        x = 0
        y = random.randint(0, screen_height - 30)
    elif num == 3:
        x = screen_width - 30
        y = random.randint(0, screen_height - 30)
    else:
        x = random.randint(0, screen_width - 30)
        y = screen_height - 30

    speed1 = random.randint(3, 5)
    speed2 = random.randint(3, 5)

    newPokeball = Pokeball(x, y, speed1, speed2)
    pokeballs.append(newPokeball)


def startScreen():
    startFont = pygame.font.Font("freesansbold.ttf", 40)
    start = startFont.render(f"Use Arrow Keys to Move", False, (0, 0, 0))
    gameScreen.blit(start, (160, 220))
    start = startFont.render(f"Click R to Start", False, (0, 0, 0))
    gameScreen.blit(start, (250, 270))
    pygame.display.flip()


def showScore(num):
    showFont = pygame.font.Font("freesansbold.ttf", 32)
    show = showFont.render(f"Score: {num}", True, black)
    gameScreen.blit(show, (10, 10))


def showLevel(num):
    if num <= 3:
        level = "Easy"
    elif num <= 6:
        level = "Normal"
    elif num <= 9:
        level = "Hard"
    elif num <= 12:
        level = "Super Hard"
    elif num <= 15:
        level = "Difficult"
    elif num <= 18:
        level = "Nightmare"
    else:
        level = "Insane"

    showFont = pygame.font.Font("freesansbold.ttf", 32)
    show = showFont.render(f"{level}", True, black)
    gameScreen.blit(show, (10, 50))


# runs
if __name__ == "__main__":

    pygame.init()

    # Initialize variables:
    clock = pygame.time.Clock()
    fps = 60
    screen_width = 800
    screen_height = 608
    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dodge The PokeBalls")
    backgroundImage = pygame.image.load("grassBackground.png")

    # colors
    red = 255, 0, 0
    blue = 0, 0, 255
    green = 0, 255, 0
    yellow = 255, 255, 0
    white = 226, 226, 226
    black = 51, 51, 51

    # init player
    initialX = screen_width / 2
    initialY = screen_height / 2
    initialSpeed = 5
    pikachu = Pikachu(initialX, initialY, initialSpeed)

    pokeballs = []
    pokeballSpawnTime = [10]
    for number in range(500, 50001, 500):
        pokeballSpawnTime.append(number)

    score = 0
    count = 0

    gameLevel = 1

    # game loop
    pause = True
    while True:

        gameScreen.fill(black)
        gameScreen.blit(backgroundImage, (0, 0))

        for event in pygame.event.get():  # quit game
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_r:  # reset the game
                pause = False

                gameLevel = 1

                pikachu.x = initialX
                pikachu.y = initialY
                pikachu.speed = initialSpeed
                score = 0
                count = 0
                pokeballs = []

        # update score
        showScore(score)
        showLevel(len(pokeballs))

        # shows game-over screen
        if pause:
            startScreen()
            continue

        # move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if pikachu.y <= 0:
                pikachu.y = pikachu.y
            else:
                pikachu.update('N')
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if pikachu.x <= 0:
                pikachu.x = pikachu.x
            else:
                pikachu.update('W')
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if pikachu.y >= screen_height - 60:
                pikachu.y = pikachu.y
            else:
                pikachu.update('S')
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if pikachu.x >= screen_width - 60:
                pikachu.x = pikachu.x
            else:
                pikachu.update('E')

        # spawn pokeballs
        for spawnTime in pokeballSpawnTime:
            if spawnTime == score:
                spawnPokeball()

        # Update game objects
        for pokeball in pokeballs:
            if pokeball.x < 0 or pokeball.x > screen_width - 30:
                pokeball.speedX *= -1
            if pokeball.y < 0 or pokeball.y > screen_height - 30:
                pokeball.speedY *= -1
            pokeball.update(pokeball.speedX, pokeball.speedY)

        # game time
        count += 1
        score = count

        # All the drawing
        pikachu.draw(gameScreen, pikachu.x, pikachu.y)
        for pokeball in pokeballs:
            pokeball.draw(gameScreen, pokeball.x, pokeball.y)

        # Check for collisions
        if collisions():
            pause = True

        pygame.display.flip()
        clock.tick(fps)
