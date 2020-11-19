import abc
from Elevator import Elevator


class AbsFloorButtons(metaclass=abc.ABCMeta):
    """
    Abstract class for floor buttons
    """
    def __init__(self, elevator: Elevator):
        self._elevator: Elevator = elevator

    @abc.abstractmethod
    def request_elevator_at(self, floor_number: int):
        """
        Call for an elevator
        :param floor_number:
        :return:
        """
        pass
