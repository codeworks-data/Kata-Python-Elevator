from time import sleep

from AbstractDoor import AbstractDoor
from DoorWithSensorWhileClosing import DoorWithSensorWhileClosing


class Elevator:
    def __init__(self):
        self._current_floor = 0
        self._door: AbstractDoor = DoorWithSensorWhileClosing()

    def get_door(self):
        """
        Getter for the attribute _door
        :return: Door
        """
        return self._door

    def get_current_floor(self) -> int:
        """
        Getter for _current_floor
        :return: int
        """
        return self._current_floor

    def go_to_floor(self, floor_number: int):
        """
        Move the elevator to the requested floor
        :return: None
        """
        self._current_floor = floor_number
        print(f'\nElevator stopping at floor: {self._current_floor}')
        self._door.open_door()
        sleep(1)
        self._door.close_door()
