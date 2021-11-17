from Elevator import elevator

class building():
    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._maxFloor = _maxFloor
        self._minFloor = _minFloor
        self._elevators = []
        for item in _elevators:
            self._elevators.append(elevator(_id = item["_id"], _speed = item["_speed"], _minFloor = item["_minFloor"], _maxFloor = item["_maxFloor"], _closeTime = item["_closeTime"], _openTime = item["_openTime"], _startTime = ["_startTime"], _stopTime = ["_stopTime"]))

    def numberOfElevetors(self):
        return len(self._elevators)

    def MaxFloor(self):
        return self._maxFloor

    def MinFloor(self):
        return self._minFloor

    def getElevetor(self, index):
        return self._elevators[index]

