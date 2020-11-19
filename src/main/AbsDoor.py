import abc

from enums import DoorStatus


class AbsDoor(metaclass=abc.ABCMeta):
    """
    Abstract class for Door
    """

    def __init__(self):
        self._status = DoorStatus.CLOSED

    @property
    def status(self):
        return self._status

    def open_door(self):
        """
        Open the door
        :return: None
        """
        self._status = DoorStatus.OPEN
        print(f'The door is now {self._status}!')

    @abc.abstractmethod
    def close_door(self):
        """
        Close the door
        :return: None
        """
        pass
