from Elevator import Elevator
from AbsFloorButtons import AbsFloorButtons
from FloorButtonsVanilla import FloorButtonsVanilla
from AbsElevatorButtons import AbsElevatorButtons
from ElevatorButtonsVanilla import ElevatorButtonsVanilla


if __name__ == '__main__':

    elevator: Elevator = Elevator()
    floor_buttons: AbsFloorButtons = FloorButtonsVanilla(elevator)
    elevator_buttons: AbsElevatorButtons = ElevatorButtonsVanilla(elevator)

    floor_buttons.request_elevator_at(2)
    elevator_buttons.request_floor(3)