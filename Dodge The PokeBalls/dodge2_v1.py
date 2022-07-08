# imports
import pygame

from pikachu import Pikachu
from pokeball import Pokeball


def collisions():
    for i in pokeballs:
        if i.collided(pikachu.rect):
            return True
    return False


def spawnPokeball():
    newPokeball = Pokeball(10, 10, 3, 3)
    pokeballs.append(newPokeball)


def startScreen():
    startFont = pygame.font.Font("freesansbold.ttf", 40)
    start = startFont.render(f"Hold SpaceBar to Fly", False, (0, 0, 0))
    gameScreen.blit(start, (180, 200))
    start = startFont.render(f"Click R to Start", False, (0, 0, 0))
    gameScreen.blit(start, (240, 250))
    pygame.display.flip()


def showScore(num):
    showFont = pygame.font.Font("freesansbold.ttf", 32)
    show = showFont.render(f"Score: {num}", True, yellow)
    gameScreen.blit(show, (10, 10))


# runs
if __name__ == "__main__":

    pygame.init()

    # Initialize variables:
    clock = pygame.time.Clock()
    fps = 60
    screen_width = 800
    screen_height = 600
    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dodge")
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
        # if collisions():
        #     pause = True

        pygame.display.flip()
        clock.tick(fps)
