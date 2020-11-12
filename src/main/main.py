from Elevator import Elevator
from FloorButtons import FloorButtons
from ElevatorButtons import ElevatorButtons


if __name__=='__main__':

    elevator = Elevator()
    elevator_buttons = ElevatorButtons(elevator)
    floor_buttons = FloorButtons(elevator)

    # Request one
    floor_buttons.call_at_floor(2)
    elevator_buttons.push_button(3)
    # Request two
    floor_buttons.call_at_floor(1)
    elevator_buttons.push_button(0)
    # Request three
    floor_buttons.call_at_floor(0)
    elevator_buttons.push_button(3)
