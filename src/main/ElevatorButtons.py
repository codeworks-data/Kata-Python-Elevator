from Elevator import Elevator
from AbstractElevatorButtons import AbstractElevatorButtons


class ElevatorButtons(AbstractElevatorButtons):
    
    def __init__(self, elevator: Elevator):
        super().__init__(elevator)

    def push_button(self, floor_number: int):
        """
        push a button of a floor number
        :param floor_number: int
        :return: None
        """
        self.elevator.go_to_floor(floor_number)
