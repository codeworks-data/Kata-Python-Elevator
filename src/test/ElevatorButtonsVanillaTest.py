import unittest
from unittest.mock import patch
from ElevatorButtonsVanilla import ElevatorButtonsVanilla
from Elevator import Elevator


class ElevatorButtonsVanillaTest(unittest.TestCase):

    def test_request_floor_should_call_go_to_floor(self):
        # Given
        with patch('__main__.Elevator') as MockElevator:
            elevator_instance = MockElevator.return_value
        requested_floor = 3
        elevator_buttons_instance = ElevatorButtonsVanilla(elevator_instance)

        # When
        elevator_buttons_instance.request_floor(requested_floor)

        # Then
        elevator_instance.go_to_floor.assert_called_with(requested_floor)


if __name__ == '__main__':
    unittest.main()
