import abc

from Elevator import Elevator


class AbsElevatorButtons(metaclass=abc.ABCMeta):
    """
    Abstract class for elevator buttons
    """
    def __init__(self, elevator: Elevator):
        self._elevator: Elevator = elevator

    @abc.abstractmethod
    def request_floor(self, floor_number: int):
        """
        Request a floot
        :param floor_number: int, floor number
        :return:
        """
        pass
