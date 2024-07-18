from typing import Optional
from queue import Queue

import pygame.mixer_music

from .struct import Music, Album


class MusicPlayer:
    def __init__(self) -> None:
        self._current_playing: Optional[Music] = None
        self._queue: Queue[Music] = Queue()

    def queue_music(self, *music_or_albums: Music | Album):
        for item in music_or_albums:
            if isinstance(item, Music):
                self._queue.put(item)

            elif isinstance(item, Album):
                for music in Album.music_list:
                    self._queue.put(music)

            else:
                raise RuntimeError

    def update(self) -> None:
        # music is not playing
        if pygame.mixer_music.get_pos() < 0:
            self._current_playing = None

            # is queue empty????
            if not self._queue.empty():
                self._current_playing = self._queue.get()
                pygame.mixer_music.load(self._current_playing.path)
                pygame.mixer_music.play()
