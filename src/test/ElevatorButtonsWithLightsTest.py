import unittest
from unittest.mock import patch

from ElevatorButtonsWithLights import ElevatorButtonsWithLights


class ElevatorButtonsTest(unittest.TestCase):

    def test_elevator_buttons_should_call_go_to_floor(self):
        with patch('main.Elevator') as MockClass:
            elevator_instance = MockClass.return_value
        requested_floor = 3

        floor_buttons_instance = ElevatorButtonsWithLights(elevator_instance)
        floor_buttons_instance.push_button(requested_floor)

        elevator_instance.go_to_floor.assert_called_with(requested_floor)


if __name__ == '__main__':
    unittest.main()
