

import pygame
import random
pygame.init()

clock = pygame.time.Clock()
Height = 400
Width = 500
Window = pygame.display.set_mode((Width, Height))
player = pygame.Rect(0, 0, 25, 25)
speed = 25
momentum = 1
Score = 0
Apple = pygame.Rect(random.randrange(0, 475, 15), random.randrange(0, 375, 15), 25, 25)
Top = pygame.Rect(0, -5, Width, 4)
Bottom = pygame.Rect(0, Height + 1, Width, 4)
Left = pygame.Rect(-5, 0, 4, Height)
Right = pygame.Rect(Width + 5, 0, 4, Height)

Running = True
while Running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    keys = pygame.key.get_just_pressed()
    
    if momentum == 1:
        if keys[pygame.K_RIGHT]:
            momentum = 1
        elif keys[pygame.K_UP]:
            momentum = 3
        elif keys[pygame.K_DOWN]:
            momentum = 4
    
    if momentum == 2:
        if keys[pygame.K_LEFT]:
            momentum = 2
        elif keys[pygame.K_UP]:
            momentum = 3
        elif keys[pygame.K_DOWN]:
            momentum = 4
    
    if momentum == 3:
        if keys[pygame.K_UP]:
            momentum = 3
        elif keys[pygame.K_LEFT]:
            momentum = 2
        elif keys[pygame.K_RIGHT]:
            momentum = 1
    
    if momentum == 4:
        if keys[pygame.K_DOWN]:
            momentum = 4
        elif keys[pygame.K_LEFT]:
            momentum = 2
        elif keys[pygame.K_RIGHT]:
            momentum = 1
    
    if momentum == 1:
        player.x += speed
    if momentum == 2:
        player.x -= speed
    if momentum == 3:
        player.y -= speed
    if momentum == 4:
        player.y += speed
    
    if player.colliderect(Apple):
        Apple.x = (random.randrange(0, 475, 15))
        Apple.y = (random.randrange(0, 375, 15))
        player = player
        Score += 1
    
    if player.colliderect(Top) or player.colliderect(Bottom) or player.colliderect(Left) or player.colliderect(Right):
        Running = False
    
    
    line_color = (40,130,40)
    background = (40,150,40)
    Window.fill(background)
    pygame.draw.rect(Window, 'blue', player)
    pygame.draw.rect(Window, 'red', Apple)
    pygame.display.flip()
    clock.tick(10)
    pygame.display.update()


print(Score)