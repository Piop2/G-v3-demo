from __future__ import annotations

from .._states.base import BaseState

# ms
_click_detect_time = 0


class CommandState(BaseState):
    def mouse_down(self) -> BaseState:
        return super().mouse_down()

    def mouse_up(self) -> BaseState:
        return super().mouse_up()


class CommandNoneState(BaseState):
    pass


class CommandClickState(CommandState):
    pass


class CommandDragStartState(CommandState):
    pass


class CommandDragEndState(CommandState):
    pass


COMMAND_NONE_STATE = CommandNoneState()
COMMAND_CLICK_STATE = CommandClickState()
COMMAND_DRAG_START_STATE = CommandDragStartState()
COMMAND_DRAG_END_STATE = CommandDragEndState()


def get_command_state() -> CommandState:
    return COMMAND_NONE_STATE


def set_click_detect_time(time: int) -> None:
    """set the time to detect clicks and drags

    Args:
        time: click detect time (ms)
    """
    global _click_detect_time
    _click_detect_time = time
