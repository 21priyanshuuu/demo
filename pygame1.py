import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

last_button_press_time = 0
current_time = 0
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            last_button_press_time = pygame.time.get_ticks()
            screen.fill((255, 255, 255))

    current_time = pygame.time.get_ticks()
    
    if current_time - last_button_press_time > 2000:
        screen.fill((0, 0, 0))
    
    print(f"current time is: {current_time}, last button press time: {last_button_press_time}")
    
    pygame.display.flip()
    clock.tick(60)
