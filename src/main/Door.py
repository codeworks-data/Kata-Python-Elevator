from DoorStatus import DoorStatus
from AbstractDoor import AbstractDoor


class Door(AbstractDoor):
    def __init__(self):
        super()

    def open_door(self):
        """
        Open the door
        :return: None
        """
        self.set_status(DoorStatus.OPEN)

    def close_door(self):
        """
        Close the door
        :return: None
        """
        self.set_status(DoorStatus.CLOSED)
