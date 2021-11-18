from Calls import calls

class elevator():
    UP = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime,_startTime, _stopTime):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime
        self._call_list = []
        self.pos = 0

    def UpdateListOfCalls(self, call):
        self._call_list.append(call)

    def getID(self):
        return (int)(self._id)

    def getSpeed(self):
        return (float)(self._speed)

    def getMinFloor(self):
        return (int)(self._minFloor)

    def getMaxFloor(self):
        return (int)(self._maxFloor)

    def gettimeForOpen(self):
        return (float)(self._openTime)

    def gettimeForClose(self):
        return (float)(self._closeTime)

    def getState(self):
        if len(self._call_list) == 0:
            return self.LEVEL
        if self._call_list[len(self._call_list) - 1].getType() is calls.UP:
            return self.UP
        elif self._call_list[len(self._call_list) - 1].getType() is calls.DOWN:
            return self.DOWN
        return self.LEVEL

    def getPos(self):

        return self.pos

    def getStartTime(self):
        return (float)(self._startTime)

    def getStopTime(self):
        return (float)(self._stopTime)

    def __str__(self):
        return f"elevator number {self._id}: \n\t speed = {self._speed} \n\t minFloor = {self._minFloor} \n\t" \
               f"maxFloor = {self._maxFloor} \n\t close time = {self._closeTime} \n\t" \
               f"open time = {self._openTime} \n\t start time = {self._startTime} \n\t" \
               f"stop time = {self._stopTime}"