from __future__ import annotations

from pygame import Vector2

from .._states.base import BaseState
from .._events import post_vision_mouse_up, post_vision_mouse_down


class VisionMouseState(BaseState):
    def mouse_down(self, pos: Vector2) -> BaseState:
        return super().mouse_down()

    def mouse_up(self, pos: Vector2) -> BaseState:
        return super().mouse_up()


class VisionMouseDownState(VisionMouseState):
    def mouse_down(self, pos: Vector2) -> BaseState:
        return self

    def mouse_up(self, pos: Vector2) -> BaseState:
        post_vision_mouse_up(pos)
        return VISION_MOUSE_UP_STATE


class VisionMouseUpState(VisionMouseState):
    def mouse_down(self, pos: Vector2) -> BaseState:
        post_vision_mouse_down(pos)
        return VISION_MOUSE_DOWN_STATE

    def mouse_up(self, pos: Vector2) -> BaseState:
        return self


VISION_MOUSE_DOWN_STATE = VisionMouseDownState()
VISION_MOUSE_UP_STATE = VisionMouseUpState()


def get_vision_mouse_state() -> VisionMouseState:
    return VISION_MOUSE_UP_STATE
