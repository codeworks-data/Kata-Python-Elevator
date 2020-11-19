from enums import DoorStatus
from AbsDoor import AbsDoor


class DoorVanilla(AbsDoor):
    """
    Vanilla door, opens and closes door the siplest way
    """
    def __init__(self):
        super().__init__()

    def close_door(self):
        """
        Simply close the door
        :return: None
        """
        self._status = DoorStatus.CLOSED
        print(f'The door is now {self._status}!')
