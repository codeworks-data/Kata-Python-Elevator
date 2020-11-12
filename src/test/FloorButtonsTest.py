import unittest
from unittest.mock import patch
from FloorButtons import FloorButtons


class FloorButtonsTest(unittest.TestCase):
    def test_floor_buttons_should_call_go_to_floor(self):
        with patch('main.Elevator') as MockClass:
            elevator_instance = MockClass.return_value
        requested_floor = 3

        floor_buttons_instance = FloorButtons(elevator_instance)
        floor_buttons_instance.call_at_floor(requested_floor)

        elevator_instance.go_to_floor.assert_called_with(requested_floor)


if __name__ == '__main__':
    unittest.main()
