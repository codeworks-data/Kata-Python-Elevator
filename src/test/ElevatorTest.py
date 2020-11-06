import unittest
from unittest.mock import patch

from Elevator import Elevator
from DoorStatus import DoorStatus


class ElevatorTest(unittest.TestCase):
    elevator = Elevator()

    def test_elevator_should_go_to_requested_floor(self):

        requested_floor = 4

        self.elevator.go_to_floor(requested_floor)
        floor_after_request = self.elevator.get_current_floor()

        self.assertEqual(floor_after_request, requested_floor)

    def test_elevator_should_open_door(self):
        requested_floor = 3

        with patch('__main__.ElevatorTest.elevator._door') as door_object:
            self.elevator.go_to_floor(requested_floor)
            door_object.set_status.assert_any_call(DoorStatus.OPEN)

    def test_door_of_elevator_should_be_closed_after_go_to_floor(self):
        requested_floor = 4

        self.elevator.go_to_floor(requested_floor)
        door_after_request = self.elevator.get_door()
        door_status_after_request = door_after_request.get_status()

        self.assertEqual(door_status_after_request, DoorStatus.CLOSED)


if __name__ == '__main__':
    unittest.main()
