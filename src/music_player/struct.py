from __future__ import annotations

from dataclasses import dataclass, field

from pygame import Surface


@dataclass
class Music:
    path: str
    title: str
    artist: Artist
    album: Album
    track_number: int


@dataclass
class Album:
    title: str
    artist: Artist
    cover_image: Surface
    music_list: list[Music] = field(default_factory=list)


@dataclass
class Artist:
    name: str
    album_list: list[Album] = field(default_factory=list)

    @property
    def music_list(self) -> list[Music]:
        return [music for album in self.album_list for music in album.music_list]
