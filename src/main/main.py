from Elevator import Elevator
from FloorButtons import FloorButtons


if __name__=='__main__':

    elevator = Elevator()
    floor_bottons = FloorButtons(elevator)

    # Request one
    floor_bottons.call_at_floor(2)
    elevator.go_to_floor(3)
    # Request two
    floor_bottons.call_at_floor(1)
    elevator.go_to_floor(0)
    # Request three
    floor_bottons.call_at_floor(0)
    elevator.go_to_floor(3)
