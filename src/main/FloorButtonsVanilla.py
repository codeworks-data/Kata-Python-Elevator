from Elevator import Elevator
from AbsFloorButtons import AbsFloorButtons


class FloorButtonsVanilla(AbsFloorButtons):
    """
    Concrete Floor Buttons class
    """
    def __init__(self, elevator: Elevator):
        super().__init__(elevator)

    def request_elevator_at(self, floor_number: int):
        """
        Call for an elevator
        :param floor_number:
        :return:
        """
        self._elevator.go_to_floor(floor_number)
