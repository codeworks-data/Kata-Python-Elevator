import abc
from Elevator import Elevator


class AbsFloorButtons:

    def __init__(self, elevator: Elevator):
        self._elevator: Elevator = Elevator()

    @abc.abstractmethod
    def request_elevator_at(self, floor_number: int):
        """
        Call for an elevator
        :param floor_number:
        :return:
        """
        pass
