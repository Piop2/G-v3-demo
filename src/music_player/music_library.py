import os
from io import BytesIO

import eyed3
import pygame

from .struct import Music, Album, Artist

_MUSIC_PATH = "./music/"


class MusicLibrary:
    def __init__(self) -> None:
        self._music: tuple[Music] = ()

    @property
    def music(self) -> list[Music]:
        return self._music

    def load_music(self) -> None:
        music_list: list[Music] = []
        album_dict: dict[str:Album] = {}
        artist_dict: dict[str:Artist] = {}

        for filename in os.listdir(_MUSIC_PATH):
            if not filename.split(".")[-1] == "mp3":
                continue

            file_path = os.path.join(_MUSIC_PATH, filename)
            audio_file = eyed3.load(file_path)

            title: str | None = audio_file.tag.title
            if title is None:
                title = filename.split(".")[0]

            artist_name: str = audio_file.tag.artist
            try:
                artist = artist_dict[artist_name]
            except KeyError:
                artist = Artist(artist_name)
                artist_dict[artist_name] = artist

            album_title: str = audio_file.tag.album
            try:
                album = album_dict[album_title]
            except KeyError:
                cover_image = pygame.image.load(
                    BytesIO(audio_file.tag.images.get("").image_data)
                )

                album = Album(title=album_title, artist=artist, cover_image=cover_image)
                album_dict[album_title] = album

                artist.album_list.append(album)

            music = Music(
                path=file_path,
                title=title,
                artist=artist,
                album=album,
                track_number=audio_file.tag.track_num.count,
            )

            album.music_list.append(music)
            music_list.append(music)
        self._music = tuple(music_list)
