import pygame, sys, random
from pygame import mixer
from random import randint
import time

#mixer.init()
#intro = pygame.mixer.Sound("../sounds/Intro.mp3")
#intro.play()

icon = pygame.image.load("../graphics/dog.png")

pygame.display.set_caption("Duck Hunt")
pygame.display.set_icon(icon)

class Crosshair(pygame.sprite.Sprite):
    
    def __init__(self, picture_path):
        
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("../sounds/Sounds_shot.wav")
        self.honk = pygame.mixer.Sound("../sounds/honk.mp3")
        
    def shoot(self):
        
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, duck_group, True)
    
    def update(self):
        
        self.rect.center = pygame.mouse.get_pos()
        
class Duck(pygame.sprite.Sprite):
    
    def __init__(self, picture_path, pos_x, pos_y):
        
        super().__init__()
        
        self.sprites = []
        self.sprites.append(pygame.image.load("../graphics/black/duck1.png"))
        self.sprites.append(pygame.image.load("../graphics/black/duck2.png"))
        self.sprites.append(pygame.image.load("../graphics/black/duck3.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]   
        self.rect.x += randint(-1, 1)
        self.rect.y += randint(-1, 1)
        self.direction = 1  
        x = random.choice([0, screen.get_width()])
        y = random.randint(0, screen.get_height() / 2)
        self.position = x, y
        self.move = [None, None]
        self.direction = None
        self.dir = randint(1, 8)
    
    def update(self):
            
        self.current_sprite += 1
        
        if self.current_sprite >= len(self.sprites):
            
            self.current_sprite = 0
        
        self.image = self.sprites[self.current_sprite]
        
        if self.dir == 1: #Moving up
            
            self.rect.y+=3;
            
            if self.rect.y == 480:
                
                self.dir == randint(2, 8)

        if self.dir == 2: #Moving down
            
            self.rect.y-=3;
            
            if self.rect.y == 1:
                
                self.dir == randint(3, 8)
        
        if self.dir == 3: #Moving left
            
            self.rect.x-=3;
            
            if self.rect.x == 640:
                
                self.dir == randint(4, 8)
        
        if self.dir == 4: #Moving right
            
            self.rect.x+=3;
            
            if self.rect.x == 1:
                
                self.dir == randint(5, 8)
            
        if self.dir == 5: #MovingSouthEast
            
            self.rect.y += 3;
            self.rect.x += 3;
            
            if self.rect.y == 1 or self.rect.x == 1:
                
                self.dir == 1
            
        if self.dir == 6: #MovingSouthWest
            
            self.rect.y += 3;
            self.rect.x -= 3;
            
            if self.rect.y == 1 or self.rect.x == 640:
                
                self.dir == randint(1, 5)
            
        if self.dir == 7: #MovingNorthWest:
            
            self.rect.y -= 3;
            self.rect.x -= 3;
            
            if self.rect.y == 480 or self.rect.x == 640:
                
                self.dir == randint(1, 5)
            
        if self.dir == 8: #MovingNorthEast:
            
            self.rect.y -= 3;
            self.rect.x += 3;      
            
            if self.rect.y == 480 or self.rect.x == 1:
                
                self.dir == randint(1, 5)
            
pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("../graphics/background.png")
foreground = pygame.image.load("../graphics/foreground.png")
bar = pygame.image.load("../graphics/bar.png")
white_icon = pygame.image.load("../graphics/white_icon.png")

shoot = 10

pygame.mouse.set_visible(False)

crosshair = Crosshair("../graphics/cursor.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

duck_group = pygame.sprite.Group()

game_start = True

game_start = False

for duck in range(10):
    
    duck_x = randint(320, 400)
    duck_y = randint(240, 300)    
    new_duck = Duck("../graphics/black/duck1.png", duck_x, duck_y)
    duck_group.add(new_duck) 
    
if pygame.sprite.spritecollideany(crosshair, duck_group):
    
    shoot -= 1
    
    
elif shoot == 8:
    
    bar_2 = pygame.image.load("../graphics/white_8.png")
    screen.blit(bar_2, (220, 410))
    
#points = 0
    
#font = pygame.font.Font("../fonts/Silkscreen/Silkscreen-Regular.ttf", 10)

#score = font.render(str(points), False, white)
#score_rect = score.get_rect()

#screen.blit(score, (0, 0))
    
#for event in pygame.event.get():
    
#    if event.type == pygame.MOUSEBUTTONDOWN:
        
#        if new_duck.collidepoint(event.pos):
            
#            points += 1
    
def update():
    
    duck_x.update()
    duck_y.update()

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 80)

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            crosshair.shoot()
            
        if event.type == timer_event:
            
            duck_group.update()
        
        pygame.display.flip()
        screen.blit(background, (0, 0))
        screen.blit(foreground, (0, 212))
        screen.blit(bar, (220, 410))     
        duck_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        clock.tick(60)