import unittest
from unittest.mock import patch
from Elevator import Elevator


class ElevatorTest(unittest.TestCase):

    elevator = Elevator()

    def test_go_to_floor_should_change_current_floor(self):
        # Given
        requested_floor = 5

        # When
        self.elevator.go_to_floor(requested_floor)
        actual_floor = self.elevator.current_floor

        # Then
        self.assertEqual(requested_floor, actual_floor)

    def test_go_to_floor_should_open_door(self):

        # Given
        requested_floor = 5

        # When
        with patch('__main__.ElevatorTest.elevator._door') as door_object:
            self.elevator.go_to_floor(requested_floor)

            # Then
            door_object.open_door.assert_call()


if __name__ == '__main__':
    unittest.main()
