from typing import Sequence

import pygame.mixer_music

from .struct import Music


def _play_music(music: Music) -> None:
    pygame.mixer_music.load(music.path)
    pygame.mixer_music.play()


class MusicPlayer:
    def __init__(self) -> None:
        self._queue: tuple[Music] = ()

        # _current_playing: index number of current playing music
        # -1: not playing
        self._current_playing = -1

    @property
    def queue(self) -> tuple[Music]:
        return self._queue

    @property
    def current_music(self) -> tuple[Music | None, int]:
        if self._current_playing == -1:
            return None, self._current_playing
        return self._queue[self._current_playing], self._current_playing

    def play_music(self, music: Music, queue: Sequence[Music]) -> None:
        try:
            self._current_playing = queue.index(music)
        except ValueError:
            raise ValueError("This music is not in this queue")
        
        self._queue = queue

        _play_music(music)

    def next_music(self) -> bool:
        if self._current_playing == -1:
            raise RuntimeError("music has not queued")
        
        if self._current_playing == len(self._queue) - 1:
            return
        
        self._current_playing += 1
        
        music, _ = self.current_music
        _play_music(music)

    def prev_music(self) -> bool:
        if self._current_playing == -1:
            raise RuntimeError("music has not queued")
        
        if self._current_playing == 0:
            return
        
        self._current_playing -= 1
        
        music, _ = self.current_music
        _play_music(music)

    def update(self) -> None:
        # music is not playing
        if pygame.mixer_music.get_pos() < 0:
            if self._current_playing == len(self._queue) - 1:
                self._current_playing = -1
            else:
                self.next_music()
