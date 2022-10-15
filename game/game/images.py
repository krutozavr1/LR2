import pygame

back_ground = [
    pygame.image.load('images/bg/plx-1.png'),
    pygame.image.load('images/bg/plx-2.png'),
    pygame.image.load('images/bg/plx-3.png'),
    pygame.image.load('images/bg/plx-4.png'),
    pygame.image.load('images/bg/plx-5.png'),
]

player_stand_right = [
    pygame.image.load('images/stand/right/Woodcutter_idle(right)_v1.png'),
    pygame.image.load('images/stand/right/Woodcutter_idle(right)_v2.png'),
    pygame.image.load('images/stand/right/Woodcutter_idle(right)_v3.png'),
    pygame.image.load('images/stand/right/Woodcutter_idle(right)_v4.png'),
]

player_stand_left = [
    pygame.image.load('images/stand/left/Woodcutter_idle_v1.png'),
    pygame.image.load('images/stand/left/Woodcutter_idle_v2.png'),
    pygame.image.load('images/stand/left/Woodcutter_idle_v3.png'),
    pygame.image.load('images/stand/left/Woodcutter_idle_v4.png')
]

player_jumping_right = [
    pygame.image.load('images/jump/right/Woodcutter_jump(right)_v1.png'),
    pygame.image.load('images/jump/right/Woodcutter_jump(right)_v2.png'),
    pygame.image.load('images/jump/right/Woodcutter_jump(right)_v3.png'),
    pygame.image.load('images/jump/right/Woodcutter_jump(right)_v4.png'),
    pygame.image.load('images/jump/right/Woodcutter_jump(right)_v5.png'),
    pygame.image.load('images/jump/right/Woodcutter_jump(right)_v6.png')
]

player_jumping_left = [
    pygame.image.load('images/jump/left/Woodcutter_jump_v1.png'),
    pygame.image.load('images/jump/left/Woodcutter_jump_v2.png'),
    pygame.image.load('images/jump/left/Woodcutter_jump_v3.png'),
    pygame.image.load('images/jump/left/Woodcutter_jump_v4.png'),
    pygame.image.load('images/jump/left/Woodcutter_jump_v5.png'),
    pygame.image.load('images/jump/left/Woodcutter_jump_v6.png'),
]

player_walk_right = [
    pygame.image.load('images/want/right/Woodcutter_walk_v1.png'),
    pygame.image.load('images/want/right/Woodcutter_walk_v2.png'),
    pygame.image.load('images/want/right/Woodcutter_walk_v3.png'),
    pygame.image.load('images/want/right/Woodcutter_walk_v4.png'),
    pygame.image.load('images/want/right/Woodcutter_walk_v5.png'),
    pygame.image.load('images/want/right/Woodcutter_walk_v6.png'),
]

player_walk_left = [
    pygame.image.load('images/want/left/Woodcutter_walk_v1.png'),
    pygame.image.load('images/want/left/Woodcutter_walk_v2.png'),
    pygame.image.load('images/want/left/Woodcutter_walk_v3.png'),
    pygame.image.load('images/want/left/Woodcutter_walk_v4.png'),
    pygame.image.load('images/want/left/Woodcutter_walk_v5.png'),
    pygame.image.load('images/want/left/Woodcutter_walk_v6.png'),
]

for image in player_stand_right:
    image.set_colorkey((0, 0, 0))
for image in player_stand_left:
    image.set_colorkey((0, 0, 0))
for image in player_jumping_right:
    image.set_colorkey((0, 0, 0))
for image in player_jumping_left:
    image.set_colorkey((0, 0, 0))
for image in player_walk_right:
    image.set_colorkey((0, 0, 0))
for image in player_walk_left:
    image.set_colorkey((0, 0, 0))
