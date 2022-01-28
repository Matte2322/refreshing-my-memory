import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

def windowSizeforRect(x, y, width, height):
    return x, y, width, height


x1 = 50
y1 = 50
width1 = 40
height1 = 60
vel1 = 5


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x1 -= vel1

    if keys[pygame.K_RIGHT]:
        x1 += vel1

    if keys[pygame.K_UP]:
        y1 -= vel1

    if keys[pygame.K_DOWN]:
        y1 += vel1
        
    
    window.fill(0,0,0)
    pygame.draw.rect(window, (255, 0, 0), windowSizeforRect(50, 50, 40, 60))
    pygame.display.update()

pygame.quit()