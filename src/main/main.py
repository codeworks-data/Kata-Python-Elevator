from Elevator import Elevator
from FloorButtons import FloorButtons
from ElevatorButtonsWithLights import ElevatorButtonsWithLights


if __name__=='__main__':

    NUMBER_OF_FLOORS = 10
    elevator = Elevator()
    elevator_buttons = ElevatorButtonsWithLights(elevator, number_of_floors=NUMBER_OF_FLOORS)
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
