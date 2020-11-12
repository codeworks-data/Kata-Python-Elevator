from Elevator import Elevator


class AbstractElevatorButtons:

    def __init__(self, elevator: Elevator):
        self.elevator = elevator

    def press_button(self, floor_number : int):
        """
        A
        :param floor_number: number of the floor to go to
        :return: None
        """
        pass
