from Elevator import Elevator
from AbsFloorButtons import AbsFloorButtons
from FloorButtonsVanilla import FloorButtonsVanilla


if __name__ == '__main__':

    elevator: Elevator = Elevator()
    floor_buttons: AbsFloorButtons = FloorButtonsVanilla(elevator)

    floor_buttons.request_elevator_at(2)
    elevator.go_to_floor(3)
