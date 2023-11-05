import pygame,sys,random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.rect=self.image.get_rect()
        self.gunshot=pygame.mixer.Sound("gunshot.wav")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)

    def update(self):
        self.rect.center=pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, target_width, target_height):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        # Scale the image to the desired width and height
        self.image = pygame.transform.scale(self.image, (target_width, target_height))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


pygame.init()
clock=pygame.time.Clock()

screen_width=865
screen_height=455
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load("bg.png")
pygame.mouse.set_visible(False)


crosshair=Crosshair("crosshair.png")
crosshair_group=pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group=pygame.sprite.Group()
for target in range(20):
    new_target = Target("target.png", random.randrange(0, screen_width), random.randrange(0, screen_height), 80, 80)
    target_group.add(new_target)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()    
    
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    pygame.display.flip()
    crosshair_group.update()
    clock.tick(60)

           
