from Elevator import elevator

class building():
    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._maxFloor = _maxFloor
        self._minFloor = _minFloor
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

    def __str__(self):
        return f"{type(self._elevators_list)} \n building: maxFloor -> {self._maxFloor} \t minFloor -> {self._minFloor} \t number of elevator -> {self.numberOfElevetors()} \t" \
               f" list of elevator -> {self._elevators_list[0]}"

