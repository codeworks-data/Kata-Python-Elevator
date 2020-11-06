from Elevator import Elevator


class FloorButtons:
    def __init__(self, elevator: Elevator):
        self.elevator = elevator

    def call_at_floor(self, floor_number: int):
        """
        Simulate a human asking for the elevator at the corresponding floor
        :param floor_number: the floor at which the elevator was requested
        :return:
        """
        self.elevator.go_to_floor(floor_number)
