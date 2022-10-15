import pygame
import images


def draw_window():
    global anim_count
    for i in range(4):
        win.blit(back_grounds[i], (0, 0))
        win.blit(back_grounds[i], (380, 0))
    if anim_count == 24:
        anim_count = 0
    if stand:
        win.blit(player_stand[right][anim_count // 6], (x, y))
    elif is_jump:
        win.blit(player_jumping[right][anim_count // 4], (x, y))
    else:
        win.blit(player_walk[right][anim_count // 4], (x, y))
    pygame.display.update()
    win.blit(back_grounds[0], (0, 0))
    anim_count += 1


pygame.init()

win = pygame.display.set_mode((760, 200))
pygame.display.set_caption('my_game')

x = 20
y = 169
width = 25
height = 31
speed = 3
jump_count = 8
stand = True
right = True
is_jump = False
anim_count = 0
clock = pygame.time.Clock()

player_walk = [images.player_walk_left, images.player_walk_right]
player_stand = [images.player_stand_left, images.player_stand_right]
player_jumping = [images.player_jumping_left, images.player_jumping_right]
back_grounds = images.back_ground


run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and speed < x:
        x -= speed
        stand = False
        right = False

    if keys[pygame.K_d] and x < 760 - width - speed:
        x += speed
        stand = False
        right = True

    if keys[pygame.K_a] and keys[pygame.K_d]:
        stand = True

    if keys[pygame.K_SPACE]:
        anim_count = 0
        is_jump = True
        stand = False

    if is_jump:
        if jump_count >= -8:
            if jump_count < 0:
                y += jump_count ** 2 / 6
            else:
                y -= jump_count ** 2 / 6
            jump_count -= 1
        else:
            jump_count = 8
            is_jump = False
            stand = True
    draw_window()
    stand = True

pygame.quit()
