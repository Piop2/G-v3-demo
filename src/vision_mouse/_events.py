import pygame.event
from pygame import Event, Vector2
from .constants import *


def post_vision_mouse_motion(pos: Vector2, dpos: Vector2, dist: int) -> None:
    """post vision mouse motion event

    Args:
        pos: vision mouse position
        dpos: vision mouse positin which relative to previous
        dist: distance of thumb tip and index finger tip
    """
    pygame.event.post(
        Event(VISIONMOUSEMOTION, {"pos": pos, "dpos": dpos, "dist": dist})
    )


def post_vision_mouse_down(pos: Vector2) -> None:
    """post vision mouse down event

    Args:
        pos: vision mouse position
    """
    pygame.event.post(Event(VISIONMOUSEDOWN, {"pos": pos}))


def post_vision_mouse_up(pos: Vector2) -> None:
    """post vision mouse up event

    Args:
        pos: vision mouse position
    """
    pygame.event.post(Event(VISIONMOUSEUP, {"pos": pos}))


def post_vision_mouse_click(pos: Vector2) -> None:
    """post vision mouse click event

    Args:
        pos: vision mouse position
    """
    pygame.event.post(Event(VISIONMOUSECLICK, {"pos": pos}))


def post_vision_mouse_drag_start(pos: Vector2) -> None:
    """post vision mouse drag start event

    Args:
        pos: vision mouse position
    """
    pygame.event.post(Event(VISIONMOUSEDRAGSTART, {"pos": pos}))


def post_vision_mouse_drag_end(pos: Vector2) -> None:
    """post vision mouse drag end event

    Args:
        pos: vision mouse position
    """
    pygame.event.post(Event(VISIONMOUSEDRAGEND, {"pos": pos}))
