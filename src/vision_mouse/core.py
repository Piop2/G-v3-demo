import warnings

import pygame
from pygame import Vector2
from pygame.camera import Camera
import mediapipe
from mediapipe.tasks.python.core.base_options import BaseOptions
from mediapipe.tasks.python.vision.core.vision_task_running_mode import (
    VisionTaskRunningMode,
)
from mediapipe.tasks.python.vision.hand_landmarker import (
    HandLandmarker,
    HandLandmarkerOptions,
)

from ._events import post_vision_mouse_motion
from ._states.mouse import get_vision_mouse_state

_HAND_LANDMARKER_MODEL_PATH = "./model/hand_landmarker.task"
_MOUSE_DOWN_RANGE = 45


class VisionMouse:
    def __init__(
        self, camera: Camera, mouse_detect_size: Vector2 | tuple[int, int]
    ) -> None:
        self._is_running = False

        self._pos = Vector2((-1, -1))

        self._vision_mouse_state = get_vision_mouse_state()

        self._camera = camera
        # self._camera.set_controls(True, False, 1)

        self._mouse_detect_size = Vector2(mouse_detect_size)

        self._hand_landmarker = HandLandmarker.create_from_options(
            HandLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=_HAND_LANDMARKER_MODEL_PATH),
                running_mode=VisionTaskRunningMode.IMAGE,
            )
        )

    @property
    def is_running(self) -> bool:
        return self._is_running

    @property
    def pos(self) -> Vector2:
        return self._pos

    @property
    def mouse_detect_size(self) -> Vector2:
        return self._mouse_detect_size

    def start(self) -> None:
        self._camera.start()
        self._camera.get_image()
        self._is_running = True

    def stop(self) -> None:
        self._camera.stop()
        self._is_running = False

    def update(self) -> None:
        if not self._is_running:
            warnings.warn(
                "VisionMouse: vision mouse was not started, use VisionMouse.start() function to start."
            )
            return

        # pygame image -> mediapipe image
        array_image = pygame.surfarray.array3d(
            pygame.transform.flip(self._camera.get_image(), True, False)
        )
        mediapipe_image = mediapipe.Image(
            image_format=mediapipe.ImageFormat.SRGB, data=array_image
        )

        # get hand landmarks
        hand_landmarker_result = self._hand_landmarker.detect(mediapipe_image)
        if not hand_landmarker_result.hand_landmarks:
            return
        if not hand_landmarker_result.handedness[0][0].category_name == "Right":
            return

        camera_size = self._camera.get_size()

        # get fingers' vector
        thumb_tip = hand_landmarker_result.hand_landmarks[0][4]
        thumb_tip_vec = pygame.Vector2(
            (camera_size[0] * thumb_tip.y, camera_size[1] * thumb_tip.x)
        )
        index_finger_tip = hand_landmarker_result.hand_landmarks[0][8]
        index_finger_tip_vec = pygame.Vector2(
            (camera_size[0] * index_finger_tip.y, camera_size[1] * index_finger_tip.x)
        )

        current_pos = (thumb_tip_vec + index_finger_tip_vec) // 2 - (
            Vector2(camera_size) // 2 - self._mouse_detect_size // 2
        )
        current_pos.x = max(0, current_pos.x)
        current_pos.x = min(self._mouse_detect_size[0], current_pos.x)
        current_pos.y = max(0, current_pos.y)
        current_pos.y = min(self._mouse_detect_size[1], current_pos.y)

        # post events
        if self._pos != current_pos:
            post_vision_mouse_motion(
                current_pos, current_pos - self._pos, current_pos.distance_to(self._pos)
            )

        if thumb_tip_vec.distance_to(index_finger_tip_vec) <= _MOUSE_DOWN_RANGE:
            self._vision_mouse_state = self._vision_mouse_state.mouse_down(current_pos)
        else:
            self._vision_mouse_state = self._vision_mouse_state.mouse_up(current_pos)

        # update mouse position
        self._pos = current_pos
