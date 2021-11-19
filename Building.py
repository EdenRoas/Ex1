from Elevator import elevator

class building():
    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._maxFloor = int(_maxFloor)
        self._minFloor = int(_minFloor)
        self._elevators_list = []
        for item in _elevators:
            self._elevators_list.append(elevator(_id=item["_id"], _speed=item["_speed"], _minFloor=item["_minFloor"],
                                                 _maxFloor=item["_maxFloor"], _closeTime=item["_closeTime"],
                                                 _openTime=item["_openTime"], _startTime=item["_startTime"],
                                                 _stopTime=item["_stopTime"]))

    def numberOfElevetors(self):
        return len(self._elevators_list)

    def MaxFloor(self):
        return self._maxFloor

    def MinFloor(self):
        return self._minFloor

    def getElevetor(self, index):
        return self._elevators_list[index]