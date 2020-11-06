from time import sleep

from Door import Door
from DoorStatus import DoorStatus


class Elevator:
    def __init__(self):
        self._current_floor = 0
        self._door: Door = Door()

    def go_to_floor(self, floor_number: int):
        """
        Move the elevator to the requested floor
        :return: None
        """
        self._current_floor = floor_number
        print(f'\nElevator stopping at floor: {self._current_floor}')
        self._door.set_status(DoorStatus.OPEN)
        sleep(1)
        self._door.set_status(DoorStatus.CLOSED)
