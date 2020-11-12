import unittest

from DoorWithSensorWhileClosing import DoorWithSensorWhileClosing
from DoorStatus import DoorStatus


class ElevatorTest(unittest.TestCase):
    door = DoorWithSensorWhileClosing()

    def test_door_should_be_open_after_call_to_open_door(self):

        self.door.open_door()
        door_status_after_request = self.door.get_status()

        self.assertEqual(door_status_after_request, DoorStatus.OPEN)

    def test_door_should_be_closed_after_call_to_close_door(self):

        self.door.set_status(DoorStatus.OPEN)
        self.door.close_door()
        door_status_after_request = self.door.get_status()

        self.assertEqual(door_status_after_request, DoorStatus.CLOSED)


if __name__ == '__main__':
    unittest.main()
