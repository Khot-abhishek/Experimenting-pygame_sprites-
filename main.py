import pygame ,sys ,random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gun_shot.mp3")
        
        
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect(center=(pos_x,pos_y))
        


pygame.init()

screen_width = 720
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('bg.png')

clock = pygame.time.Clock()


crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for i in range(20):
    x = random.randrange(10,screen_width)
    y = random.randrange(10,screen_height)
    new_target = Target('target.png',x,y)
    target_group.add(new_target)
    
game_over = pygame.image.load('game_over.png')
game_over_rect = game_over.get_rect(center=(360,200))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()    
    
    pygame.display.update()
    screen.blit(background,(0,0))
    
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    
    if not target_group.sprites():
        screen.blit(game_over,game_over_rect)
    
    
    clock.tick(60)