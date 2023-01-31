import pygame
pygame.init()
size = width, height = 300,300
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))

def isPrime(value) -> bool:
    for i in range(2,value):
        if value%i == 0:
            return False
    return True

def spiral(x = width//2,y = height//2):
    step = 1
    state = 0
    numStep = 1
    turnCounter = 0
    while True:
        if (isPrime(step)):
            screen.fill((255,255,255), ((x,y), (2, 2)))
        if state == 0: x += 5
        elif state == 1: y -= 5
        elif state == 2: x -= 5
        elif state == 3: y += 5
        #TODO: come-up with better logic
        if step % numStep == 0:
            state = (state + 1) % 4
            turnCounter += 1
            if turnCounter % 2 == 0:
                numStep += 1
        step += 1
        pygame.display.flip()
        if x > width:
            pygame.image.save(screen, 'img/surface.png')
            break

if __name__ == "__main__":
    spiral()