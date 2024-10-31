import pygame, random, time
from threading import Event
pygame.init()
clock = pygame.time.Clock()
GRAVITY = 0.7
JUMP_VELOCITY = -10
FRICTION = 0.9
ACCELERATION = 0.5
ACCELERATION_B = 0.5
gate = 2
touch = False
is_command_paused = False
lad = False
delay_duration = 100  
touch_duration = 1100  
command_start_time = pygame.time.get_ticks()
is_command_delayed = False
znacznik = 2
last_display_time = pygame.time.get_ticks()

delay = 2500
command_start = pygame.time.get_ticks()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 0
        self.x_velocity = 0
    def update(self):
        self.rect.y += self.y_velocity
        self.rect.x += self.x_velocity
        self.y_velocity += GRAVITY
        self.x_velocity *= FRICTION

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 0
        self.x_velocity = 0
        self.image.fill((255, 160, 122))
    def update(self):
        self.rect.y += self.y_velocity
        self.rect.x += self.x_velocity
        self.y_velocity += GRAVITY
        self.x_velocity *= FRICTION
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill((255, 255, 0))
    
    #def draw():
    #    coin = Coin(10, 10, 10, 10)
    #    pygame.draw.rect(screen, (255, 255, 0), coin)

class Pointer(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, opn):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill((128, 128, 128))
        self.open = opn
        

class Path(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill((255, 0, 0))

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill((139, 69, 19))

class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill((255, 105, 180))

def drawing():
    pointer_checker = 9
    pointer_checker += random.randint(0,6)
    #Event().wait(5)
    return pointer_checker
   
    
screen = pygame.display.set_mode((640, 480))
player = Player(100, 300)
player_group = pygame.sprite.Group()
player_group.add(player)


#barrel_data = [
#    (20, 65),
#    (50, 65)
#]

barrel = Barrel(20, 65)
barrel1 = Barrel(50, 65)


#coin1 = Coin(580, 250, 20, 20)
#coin2 = Coin(300, 150, 20, 20)
#coin3 = Coin(180, 250, 20, 20)
#coin4 = Coin(60, 50, 20, 20)

queen = Queen(580, 20, 50, 40)


pointer_l = Pointer(0, 0, 1, 480, 1)
pointer_r = Pointer(639, 0, 1, 480,1 )
pointer1_1 = Pointer(200, 90, 1, 10, 1)
pointer1_2 = Pointer(430, 90, 1, 10, 1)
pointer2_1 = Pointer(105, 190, 1, 10, 1)
pointer2_2 = Pointer(310, 190, 1, 10, 1)
pointer3_1 = Pointer(530, 290, 1, 10, 1)

##deklarowanie platform
ladder1_1 = Ladder(500, 300, 40, 100)
ladder2_1 = Ladder(300, 200, 40, 95)
ladder2_2 = Ladder(90, 200, 40, 95)
ladder3_1 = Ladder(170, 100, 40, 95)
ladder3_2 = Ladder(400, 100, 40, 95)

platform_data = [
    (0, 400, 640, 10),
    (0, 300, 640, 10),
    (0, 200, 640, 10),
    (0, 100, 640, 10)
]



#platform = Platform(0, 400, 640, 10)
#platform1 = Platform(0, 300, 640, 10)
#platform2 = Platform(0, 200, 640, 10)
#platform3 = Platform(0, 100, 640, 10)


path1_1 = Path(0, 395, 640, 5)
path2_1 = Path(0, 295, 500, 5)
path2_2 = Path(540, 295, 100, 5)
path3_1 = Path(0, 195, 90, 5)
path3_2 = Path(130, 195, 170, 5)
path3_3 = Path(340, 195, 320, 5)
path4_1 = Path(0, 95, 170, 5)
path4_2 = Path(210, 95, 190, 5)
path4_3 = Path(440, 95, 220, 5)

ladder_group = pygame.sprite.Group()
path_group = pygame.sprite.Group()
barrel_group = pygame.sprite.Group()
pointer_group_walls = pygame.sprite.Group()
pointer_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
queen_group = pygame.sprite.Group()

platform_group = pygame.sprite.Group()
##tu zmieniam zeby nie mozna było wchodzic na platformy od dołu
## stworzenie osobnej grupy dla platform bez prznikania
platform_group_red = pygame.sprite.Group()

# dodanie platform do grup
#platform_group.add(platform)

barrel_group.add(barrel)
barrel_group.add(barrel)

barrel_group.add(barrel)
queen_group.add(queen)

#coin_group.add(coin)
#coin_group.add(coin1)
#coin_group.add(coin2)
#coin_group.add(coin3)
#coin_group.add(coin4)

pointer_group_walls.add(pointer_l)
pointer_group_walls.add(pointer_r)
pointer_group.add(pointer1_1)
pointer_group.add(pointer1_2)
pointer_group.add(pointer2_1)
pointer_group.add(pointer2_2)
pointer_group.add(pointer3_1)

for data in platform_data:
    platform = Platform(*data)
    platform_group_red.add(platform)



floors = [70, 170, 370, 270]

while len(coin_group) < 6:
    coin = Coin(random.randint(0, 600), random.choice(list(floors)), 20, 20)
    coin_group.add(coin)


#platform_group_red.add(platform1)
#platform_group_red.add(platform2)
#platform_group_red.add(platform3)

ladder_group.add(ladder1_1)
ladder_group.add(ladder2_1)
ladder_group.add(ladder2_2)
ladder_group.add(ladder3_1)
ladder_group.add(ladder3_2)

path_group.add(path1_1)
path_group.add(path2_1)
path_group.add(path2_2)
path_group.add(path3_1)
path_group.add(path3_2)
path_group.add(path3_3)
path_group.add(path4_1)
path_group.add(path4_2)
path_group.add(path4_3)

player_movement = 0
barrel_movement = 1
points = 0
waiter = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.y_velocity = JUMP_VELOCITY
            elif event.key == pygame.K_LEFT:
                player_movement = -1
            elif event.key == pygame.K_RIGHT:
                player_movement = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_movement = 0

    current_t = pygame.time.get_ticks()

    if current_t - last_display_time >= delay:
        znacznik = random.randint(1,2)
        
        #print(current_t, command_start)
        last_display_time = current_time
        

    if waiter == 1:
        time.sleep(5)
        running = False
    player.x_velocity += player_movement * ACCELERATION
    barrel.x_velocity += barrel_movement * ACCELERATION_B
    player_group.update()
    barrel_group.update()
    collided_sprites = pygame.sprite.spritecollide(player, platform_group, False)
    collided_sprites_barrel = pygame.sprite.spritecollide(barrel, path_group, False)
    collided_sprites_pointer_walls = pygame.sprite.spritecollide(barrel, pointer_group_walls, False)
    collided_sprites_pointer_walls_p = pygame.sprite.spritecollide(player, pointer_group_walls, False)
    collided_sprites_pointer = pygame.sprite.spritecollide(barrel, pointer_group, False)
    collided_game_over = pygame.sprite.spritecollide(barrel, player_group, False)
    #collided_coin = pygame.sprite.spritecollide(player, coin_group, False)
    collided_queen = pygame.sprite.spritecollide(player, queen_group, False)
    ## tu tez zmienione
    collided_sprites_red = pygame.sprite.spritecollide(player, platform_group_red, False)
    collided_sprites_ladder = pygame.sprite.spritecollide(player, ladder_group, False)
    collided_sprites_path = pygame.sprite.spritecollide(player, path_group, False)
    
    screen.fill((128, 128, 128))
    pointer_group.draw(screen)
    ladder_group.draw(screen)
    coin_group.draw(screen)
    player_group.draw(screen)
    platform_group.draw(screen)
    platform_group_red.draw(screen)
    path_group.draw(screen)
    barrel_group.draw(screen)
    pointer_group_walls.draw(screen)
    
    queen_group.draw(screen)
    

    
    if barrel.rect.y > 360:
        barrel.rect.x = random.randint(20, 300)
        barrel.rect.y = 60
        
  
    
    
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    pointes = str(points)
    text = font.render(pointes, False, (0, 0, 0))
    screen.blit(text, (540, 30))
    


    if collided_sprites:
        player.y_velocity = 0
        #pygame.font.init()
        #font = pygame.font.SysFont('Comic Sans MS', 30)
        #text = font.render('Collision: True', False, (0, 0, 0))
        #screen.blit(text, (320, 240))

    if collided_sprites_barrel:
        barrel.y_velocity = 0

    #if collided_coin:
    #    points += 1
    coin_collision = pygame.sprite.spritecollide(player, coin_group, True)
    points += len(coin_collision)

    if collided_queen:
        #screen.fill((0))
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text = font.render('Congratulations', False, (0, 0, 0))
        screen.blit(text, (140, 100))
        waiter = 1
        
    if collided_sprites_pointer_walls_p:
        if player.rect.x < 100:
            player.x_velocity = 2
        else:
           player.x_velocity = -2 
        
    if collided_sprites_pointer_walls:
        #barrel_movement *= -1
        if barrel.rect.x > 300:
            ACCELERATION_B = -0.7
        else:
            ACCELERATION_B = 0.7
    #zna = [0, 1]
    if player.rect.y < 0:
        player.y_velocity = 2
    
    if collided_sprites_pointer and znacznik > 1:
        barrel.x_velocity = 0
        barrel.y_velocity = 2
        is_command_delayed = True         
        command_start_time = pygame.time.get_ticks()
            

    current_time = pygame.time.get_ticks()
    
    if is_command_delayed and current_time - command_start_time >= delay_duration:
        znacznik = random.randint(1,2)
        if ACCELERATION_B > 0:
            ACCELERATION_B = -0.7
        else:
            ACCELERATION_B = 0.7

        is_command_delayed = False
        #is_command_paused = False
        command_start_time = 0

    if collided_game_over:
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text = font.render('Game over', False, (0, 0, 0))
        screen.blit(text, (190, 200))
        waiter = 1
            
        

    ##dodane
    if collided_sprites_red:
        player.y_velocity = 5
        #pygame.font.init()
        #font = pygame.font.SysFont('Comic Sans MS', 30)
        #text = font.render('Collision: True', False, (0, 0, 0))
        #screen.blit(text, (320, 240))
    
    if collided_sprites_ladder:
        player.y_velocity = -2
        lad = True
        Barrel(100, 2)
    
    
    if collided_sprites_path:
        player.y_velocity = 0
        





    clock.tick(30)
    pygame.display.flip()
pygame.quit()