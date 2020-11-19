from AbsElevatorButtons import AbsElevatorButtons
from Elevator import Elevator


class ElevatorButtonsVanilla(AbsElevatorButtons):
    """
    Concrete Floor Buttons class
    """
    def __init__(self, elevator: Elevator):
        super().__init__(elevator)

    def request_floor(self, floor_number: int):
        """
        request a floor
        :param floor_number: int, floor number
        :return:
        """
        self._elevator.go_to_floor(floor_number)
