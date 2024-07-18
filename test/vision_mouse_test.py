import sys

import pygame
import pygame.camera
from pygame.locals import *

from src.vision_mouse import (
    VisionMouse,
    VISIONMOUSEMOTION,
    VISIONMOUSEDOWN,
    VISIONMOUSEUP,
)

WINDOW_SIZE = (640, 480)
FPS = 60
CAMERA_SIZE = (1280, 720)
MOUSE_DECTECT_SIZE = WINDOW_SIZE


pygame.init()
pygame.camera.init()

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.Clock()
pygame.display.set_caption("vision mouse test")

camera = pygame.camera.Camera(pygame.camera.list_cameras()[0], CAMERA_SIZE)

vision_mouse = VisionMouse(camera, MOUSE_DECTECT_SIZE)
vision_mouse.start()

mouse_pos = pygame.Vector2()
mouse_down = False

while True:
    dt = clock.tick(FPS)

    window.fill("white")

    vision_mouse.update()

    pygame.draw.circle(window, (0, 255, 0) if mouse_down else (0, 0, 0), mouse_pos, 5)

    for event in pygame.event.get():
        if event.type == QUIT:
            vision_mouse.stop()
            pygame.quit()
            sys.exit()

        if event.type == VISIONMOUSEMOTION:
            mouse_pos = event.pos

        if event.type == VISIONMOUSEDOWN:
            mouse_down = True

        if event.type == VISIONMOUSEUP:
            mouse_down = False
    pygame.display.flip()
