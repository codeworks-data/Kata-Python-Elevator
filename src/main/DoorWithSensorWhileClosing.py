from DoorStatus import DoorStatus
from AbstractDoor import AbstractDoor
import random


class DoorWithSensorWhileClosing(AbstractDoor):
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
        Chech until nobody is on the way, and then, close the door
        :return: None
        """
        # sonsor is defined by a parameter of chance.
        # there will be a person on the way one every 'times'
        times = 3
        while random.randint(0, times) != 0:
            print('Somebody is on the way, cannot close the door')
        self.set_status(DoorStatus.CLOSED)
