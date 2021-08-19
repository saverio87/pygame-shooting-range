# This is a sample Python script.
import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


# Global variables

## Background

wood_bg = pygame.image.load('assets/bg_wood.png');
land_bg = pygame.image.load('assets/grass2.png');
water_bg = pygame.image.load('assets/water1.png');
cloud1 = pygame.image.load('assets/cloud1.png');
cloud2 = pygame.image.load('assets/cloud2.png');

## X,Y coord and speed
land_speed = 1
water_speed = 2
land_pos_y = 560
water_pos_y = 640

## Cursor

crosshair = pygame.image.load('assets/crosshair.png')

## Ducks

duck_surface = pygame.image.load('assets/duck.png')
duck_list = []

for duck in range(5):
        duck_pos_x = random.randrange(50,1200)
        duck_pos_y = random.randrange(120,500)
        duck_rect = duck_surface.get_rect(center = (duck_pos_x,duck_pos_y))
        duck_list.append(duck_rect)


## Game font

game_font = pygame.font.Font(None, 120)
text_surface = game_font.render("You Won!!!", True, (255,255,255))
text_rect = text_surface.get_rect(center = (640,360))



# Draw background

def ground_animation():

    global land_pos_y, land_speed;
    
    if land_pos_y <= 520 or land_pos_y >= 600:
        land_speed *= -1   
    for x in range(0,1280,132):
        screen.blit(land_bg, (x, land_pos_y))
    land_pos_y += land_speed;


def water_animation():
    
    global water_pos_y, water_speed;
    
    if water_pos_y <= 620 or water_pos_y >= 680:
        water_speed *= -1   
    for x in range(0,1280,132):
        screen.blit(water_bg, (x, water_pos_y))
    water_pos_y += water_speed;

    

def draw_background():
    
    for y in range(0,720,256):
            for x in range(0,1280,256):
                screen.blit(wood_bg, (x,y))

    screen.blit(cloud1, (100,50))
    screen.blit(cloud2, (300,160))
    screen.blit(cloud2, (900, 100))


def generate_ducks():

    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)
    



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    duck_list.remove(duck_list[index])

        
            
    

    # Background and duck generation
            
    draw_background()
    generate_ducks()
    ground_animation()
    water_animation()


    # Draw cursor / crosshair
    
    screen.blit(crosshair, crosshair_rect)

    # Game over

    if len(duck_list) == 0:
            screen.blit(text_surface, text_rect)


    
    pygame.display.update()
    clock.tick(120)
    #Setting the frame rate to 120 frames / second



