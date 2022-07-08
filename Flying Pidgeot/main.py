import pygame
import random
from pidgeot import Pidgeot
from fearow import Fearow


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


def collisions():
    for i in fearows:
        if i.collided(pidgeot.rect):
            return True
    return False


def DeleteOutOfRange():
    pts = 0
    for i in fearows:
        if i.x < -50:
            fearows.remove(i)
            pts += 1

    return pts


def spawnFearow():
    rand = random.randint(1, 120)
    if rand == 1:
        newFearow = Fearow(screen_width, screen_height)
        fearows.append(newFearow)


# runs
if __name__ == "__main__":

    pygame.init()

    # Initialize variables:
    clock = pygame.time.Clock()
    fps = 60
    screen_width = 800
    screen_height = 500
    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Pidgeot")
    backgroundImage = pygame.image.load("skyBackground.jpg")

    # colors
    red = 255, 0, 0
    blue = 0, 0, 255
    green = 0, 255, 0
    yellow = 255, 255, 0
    white = 226, 226, 226
    black = 51, 51, 51

    # init player
    initialX = screen_width / 10
    initialY = screen_height / 4
    initialFlySpeed = 3
    addFlySpeed = 0.03
    flyDirection = 0
    pidgeot = Pidgeot(initialX, initialY, initialFlySpeed)

    fearows = []
    fearowSpeed = 2
    addSpeed = 0.05

    score = 0

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
                flyDirection = -1
                pidgeot.x = initialX
                pidgeot.y = initialY
                pidgeot.speed = initialFlySpeed
                score = 0
                fearows = []
                fearowSpeed = 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flyDirection = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    flyDirection = -1

        # update score
        showScore(score)

        # game over when pidgeot goes out the screen
        if pidgeot.y <= -30 or pidgeot.y >= screen_height - 20:
            pause = True

        # shows start screen
        if pause:
            startScreen()
            continue

        # spawn fearows and increase fearows and pidgeot speed gradually
        spawnFearow()
        chance = random.randint(1, 60)
        if chance == 1:
            fearowSpeed += addSpeed
            pidgeot.speed += addFlySpeed

        # Update game objects
        pidgeot.update(flyDirection)
        for fearow in fearows:
            fearow.update(fearowSpeed)

        # Delete all out of range objects
        score += DeleteOutOfRange()

        # drawing
        pidgeot.draw(gameScreen, pidgeot.x, pidgeot.y)
        for fearow in fearows:
            fearow.draw(gameScreen, fearow.x, fearow.y)

        # Check for collisions
        if collisions():
            pause = True

        pygame.display.flip()
        clock.tick(fps)
