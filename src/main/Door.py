from DoorStatus import DoorStatus

class Door:
    def __init__(self):
        self._status: DoorStatus = DoorStatus.CLOSED

    def get_status(self) -> DoorStatus:
        """
        Getter for status attribute
        :return: DoorStatus(enum)
        """
        return self._status

    def set_status(self, status: DoorStatus):
        """
        Setter of status attribute
        :param status: DoorStatus
        :return: None
        """
        self._status = status
        print(f'Door status is {status}')
