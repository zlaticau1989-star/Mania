import pygame
import random
import time
import os
import sys
from pygame import mixer

if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(__file__)


def get_sound_path(filename):
    return os.path.join(base_dir, "sounds", filename)


pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

mixer.music.load(get_sound_path(
    "Buddhist Monk Chant Drone backing track -  key of Gb ⧸ F#.mp3"))
mixer.music.set_volume(0.3)
mixer.music.play(-1)

pygame.mixer.set_num_channels(10)

sounds = {
    "droplet": pygame.mixer.Sound(get_sound_path("droplet.mp3")),
    "droplet2": pygame.mixer.Sound(get_sound_path("droplet2.mp3")),
    "bells": pygame.mixer.Sound(get_sound_path("bells.mp3")),
    "babycry": pygame.mixer.Sound(get_sound_path("babycry.mp3")),
    "phone": pygame.mixer.Sound(get_sound_path("phone.mp3")),
    "dial": pygame.mixer.Sound(get_sound_path("dial.mp3")),
    "womancry": pygame.mixer.Sound(get_sound_path("womancry.mp3")),
    "oldwhatever": pygame.mixer.Sound(get_sound_path("oldwhatever.mp3")),
    "belllong": pygame.mixer.Sound(get_sound_path("belllong.mp3")),
    "windbird": pygame.mixer.Sound(get_sound_path("windbird.mp3")),
    "oldrant": pygame.mixer.Sound(get_sound_path("oldrant.mp3")),
}

window = pygame.display.set_mode((500, 500))
window.fill((255, 255, 255))

drawing_layer = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
image = drawing_layer.convert_alpha()

rot = 0

color = (127, 127, 127)

player = pygame.Surface((1, 1))
player.fill(color)
window.blit(player, (0, 499))

up = []
right = []
down = []
left = []
playerX = 1
playerY = 500

lists = [[1000] for i in range(502)]

for i in range(500):
    lists[0].append(1000)
    lists[501].append(1000)

# Random Values


def appendAll(a):
    for i in range(500):
        lists[a+1].append(int(random.randint(1, 999)))


for i in range(500):
    appendAll(i)
    lists[i+1].append(1000)


def path(x, y):
    global color

    drawing_layer.blit(player, (x, y))
    drawing_layer.blit(player, (501-x, 501-y))
    drawing_layer.blit(player, (501-x, y))
    drawing_layer.blit(player, (x, 501-y))

    cc = random.randint(1, 5)
    what = random.randint(1, 3)
    what1 = random.randint(1, 2)

    if what == 1 and what1 == 1 and color[0]+cc <= 250:
        color = (color[0]+cc, color[1], color[2])
    elif what == 1 and what1 == 2 and color[0]-cc >= 5:
        color = (color[0]-cc, color[1], color[2])

    elif what == 2 and what1 == 1 and color[1]+cc <= 250:
        color = (color[0], color[1]+cc, color[2])
    elif what == 2 and what1 == 2 and color[1]-cc >= 5:
        color = (color[0], color[1]-cc, color[2])

    elif what == 3 and what1 == 1 and color[2]+cc <= 250:
        color = (color[0], color[1], color[2]+cc)
    elif what == 3 and what1 == 2 and color[2]-cc >= 5:
        color = (color[0], color[1], color[2]-cc)

    if cc == 5:
        rand = random.randint(1, 10)
        if random.randint(1, 10) == 1:
            pygame.mixer.Channel(0).play(sounds["droplet"])
        elif rand == 2:
            pygame.mixer.Channel(0).play(sounds["droplet2"])
        elif rand == 3:
            pygame.mixer.Channel(1).play(sounds["bells"])

        if random.randint(1, 1000) == 1:
            pygame.mixer.Channel(3).play(sounds["babycry"])
        if random.randint(1, 1000) == 1:
            pygame.mixer.Channel(5).play(sounds["phone"])
        if random.randint(1, 1000) == 1:
            pygame.mixer.Channel(5).play(sounds["dial"])
        if random.randint(1, 1000) == 1:
            pygame.mixer.Channel(3).play(sounds["womancry"])
        if random.randint(1, 500) == 1:
            pygame.mixer.Channel(2).play(sounds["oldwhatever"])
        if random.randint(1, 200) == 1:
            pygame.mixer.Channel(1).play(sounds["belllong"])
        if random.randint(1, 200) == 1:
            pygame.mixer.Channel(4).play(sounds["windbird"])
        if random.randint(1, 500) == 1:
            pygame.mixer.Channel(3).play(sounds["oldrant"])

    player.fill(color)


def check():
    global playerX
    global playerY

    up = int(lists[playerY-1][playerX])
    right = int(lists[playerY][playerX+1])
    down = int(lists[playerY+1][playerX])
    left = int(lists[playerY][playerX-1])

    if up < right and up < down and up < left:
        playerY -= 1
        lists[playerY+1][playerX] = 1000
        path(playerX, playerY)
    elif right < up and right < down and right < left:
        playerX += 1
        lists[playerY][playerX-1] = 1000
        path(playerX, playerY)
    elif down < up and down < right and down < left:
        playerY += 1
        lists[playerY-1][playerX] = 1000
        path(playerX, playerY)
    elif left < up and left < right and left < down:
        playerX -= 1
        lists[playerY][playerX+1] = 1000
        path(playerX, playerY)
    elif up == right == down == left:
        which = random.randint(1, 4)
        if which == 1 and playerX+1 != 501:
            lists[playerY][playerX+1] = random.randint(1, 999)
        elif which == 2 and playerY-1 != 0:
            lists[playerY-1][playerX] = random.randint(1, 999)
        elif which == 3 and playerX-1 != 0:
            lists[playerY][playerX-1] = random.randint(1, 999)
        elif which == 4 and playerY+1 != 501:
            lists[playerY+1][playerX] = random.randint(1, 999)

    else:
        which = random.randint(1, 4)
        if which == 1 and playerX+1 != 501:
            lists[playerY][playerX+1] = random.randint(1, 999)
        elif which == 2 and playerY-1 != 0:
            lists[playerY-1][playerX] = random.randint(1, 999)
        elif which == 3 and playerX-1 != 0:
            lists[playerY][playerX-1] = random.randint(1, 999)
        elif which == 4 and playerY+1 != 501:
            lists[playerY+1][playerX] = random.randint(1, 999)


while True:

    window.blit(window, (0, 0))
    window.blit(drawing_layer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    rot += 0.001
    if rot >= 360:
        rot = 0
    rotated = pygame.transform.rotate(drawing_layer, rot)

    rect = rotated.get_rect(center=(250, 250))
    window.blit(rotated, rect)

    check()
    pygame.display.update()
    clock.tick(240)
