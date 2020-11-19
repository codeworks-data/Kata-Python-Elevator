from time import sleep

from AbsDoor import AbsDoor
from DoorVanilla import DoorVanilla


class Elevator:

    def __init__(self):
        self._current_floor: int = 0
        self._door: DoorVanilla = DoorVanilla()

    @property
    def current_floor(self):
        return self._current_floor

    def go_to_floor(self, floor_number: int):
        """
        move elevator to requested floor
        :param floor_number: int, the requested floor number
        :return: None
        """

        print(f'Elevator is now on floor {floor_number}')
        self._current_floor = floor_number
        self._door.open_door()
        sleep(1)
        self._door.close_door()
