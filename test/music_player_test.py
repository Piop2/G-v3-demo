import sys

import pygame

from src.music_player import MusicPlayer, MusicLibrary

FPS = 60

pygame.init()
window = pygame.display.set_mode((100, 100))
clock = pygame.Clock()
pygame.display.set_caption("music player test")

music_player = MusicPlayer()
music_lib = MusicLibrary().load_music()

music_player.play_music(music_lib.music[0], music_lib.music)

while True:
    clock.tick(FPS)

    window.fill("white")

    music_player.update()

    print(pygame.mixer_music.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                music_player.prev_music()
            if event.key == pygame.K_d:
                music_player.next_music()
            if event.key == pygame.K_SPACE:
                pygame.mixer_music.set_pos(0)

    pygame.display.flip()
