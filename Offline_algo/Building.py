from elevator import Elevator


class Building():
    def __init__(self, _minFloor, _maxFloor, _elevators = []):
        self._maxFloor = _maxFloor
        self._minFloor = _minFloor
        self._elevator = _elevators.copy()

    def numberOfElevetors(self):
        return len(self._elevator)

    def MaxFloor(self):
        return self.maxFloor

    def MinFloor(self):
        return self.minFloor

    def getElevetor(self, index):
        return self.elevators[index]

