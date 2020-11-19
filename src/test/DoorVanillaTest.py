import unittest
from unittest.mock import patch
from DoorVanilla import DoorVanilla
from enums import DoorStatus


class DoorVanillaTest(unittest.TestCase):

    door = DoorVanilla()

    def test_open_door_should_make_status_open(self):
        # When
        self.door.open_door()
        actual_door_status = self.door.status

        # Then
        self.assertEqual(DoorStatus.OPEN, actual_door_status)

    def test_close_door_should_make_status_closed(self):
        # When
        self.door.close_door()
        actual_door_status = self.door.status

        # Then
        self.assertEqual(DoorStatus.CLOSED, actual_door_status)


if __name__ == '__main__':
    unittest.main()
