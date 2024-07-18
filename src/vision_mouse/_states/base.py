from __future__ import annotations


class BaseState:
    def mouse_down(self) -> "BaseState":
        raise NotImplementedError

    def mouse_up(self) -> "BaseState":
        raise NotImplementedError
