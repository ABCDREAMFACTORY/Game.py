import pygame
from PIL import Image
pygame.init()
fenetreHauteur = 1280
fenetreLargeur = 720
screen = pygame.display.set_mode((fenetreHauteur, fenetreLargeur))
clock = pygame.time.Clock()
running = True


class player():
    def __init__(self):
        self.co_x = 50
        self.co_y = 600
        self.score = 0
        self.skin = pygame.image.load("assets/Stand.gif")
        self.speed = 5
        self.run = False
        self.on_ground = True
        self.player_vel_y = 0
    def move_left(self):
        self.co_x -= self.speed
    def move_right(self):
        self.co_x += self.speed
    def jump(self):
        self.co_y -= self.speed
    def down(self):
        self.co_y += self.speed
    def gain_score(self,how_much):
        self.score += how_much
    def Gravity(self):
        if self.on_ground == False:
            self.player_vel_y += gravity
            self.co_y += self.player_vel_y
        if self.co_y >= ground:
            self.co_y = ground
            self.player_vel_y = 0
            self.on_ground = True
def extract_frames(path):
    with Image.open(path) as img:
        frames = []
        for frame in range(img.n_frames):
            img.seek(frame)
            frame_img = img.copy()
            frame_surface = pygame.image.fromstring(frame_img.tobytes(), frame_img.size, frame_img.mode)
            frame_surface = pygame.transform.scale(frame_surface,(200, 200))
            frames.append(frame_surface)
    return frames

Player1 = player()

player1frame = extract_frames("assets/Stand.gif")
animage_nb_image = len(player1frame) # pour un tileset de 10 images
animage_duree    = 700 # 5000ms(5secondes)
animage_laps     = animage_duree//animage_nb_image
animage_index    = 1
pygame.time.set_timer(pygame.USEREVENT, animage_laps)


bg = pygame.image.load("assets/Background2.jpg")
bg = pygame.transform.scale(bg,(fenetreHauteur, fenetreLargeur))

Player1.skin = pygame.transform.scale(Player1.skin,(200, 200))

pygame.display.set_caption("Jeu python")


gravity = 0.5
jump_strength = -10
ground = 600
start_standing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            
            animage_index = (animage_index+1)%animage_nb_image
            if animage_index == 0:
                animage_index = 1
            #Player1.skin = pygame.image.load("assets\Stand.gif")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if Player1.on_ground:
            Player1.player_vel_y = jump_strength
            Player1.on_ground = False
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        Player1.down()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        Player1.move_right()    
        player1frame = extract_frames("assets/runAnim.gif")
        start_standing = True
        animage_nb_image = len(player1frame)
    elif keys[pygame.K_q] or keys[pygame.K_LEFT]:
        Player1.move_left()
        player1frame = extract_frames("assets/runAnim.gif")
        player1frame = [pygame.transform.flip(frame, True, False) for frame in player1frame]
        animage_nb_image = len(player1frame)
        start_standing = True
        
    #if keys[pygame.K_q] == False and keys[pygame.K_d] == False and start_standing == True:
    elif start_standing == True:
        player1frame = extract_frames("assets/Stand.gif")
        animage_nb_image = len(player1frame)
        start_standing = False
        animage_index  = 1
    Player1.Gravity()

    screen.blit(bg,(0,0))
    
    rect = Player1.skin.get_rect()
    rect.center = Player1.co_x,Player1.co_y
    #screen.blit(Player1.skin,rect)
    screen.blit(player1frame[animage_index],rect)

    clock.tick(60)  # limits FPS to 60
    pygame.display.update()
