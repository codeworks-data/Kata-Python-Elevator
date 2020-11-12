from Elevator import Elevator
from AbstractElevatorButtons import AbstractElevatorButtons
from LightStatus import LightStatus


class ElevatorButtonsWithLights(AbstractElevatorButtons):

    def __init__(self, elevator: Elevator, number_of_floors: int):
        super().__init__(elevator)
        self._lights_status = [LightStatus.ON for _ in range(number_of_floors)]

    def push_button(self, floor_number: int):
        """
        push a button of a floor number
        :param floor_number: int
        :return: None
        """
        self.light_on_button(floor_number)
        self.elevator.go_to_floor(floor_number)
        self.light_off_button(floor_number)

    def light_on_button(self, floor_number: int):
        """
        Light on a button
        :param floor_number: int
        :return:
        """
        print(f'Lighting up button of floor {floor_number}!')
        self._lights_status[floor_number] = LightStatus.ON

    def light_off_button(self, floor_number: int):
        """
        Light off a button
        :param floor_number: int
        :return:
        """
        print(f'Lighting off button of floor {floor_number}!')
        self._lights_status[floor_number] = LightStatus.OFF
