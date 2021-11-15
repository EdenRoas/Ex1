class Elevator():
    UP = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

    def __init__(self, _id,_speed, _minFloor, _maxFloor, _closeTime, _openTime,_startTime, _stopTime):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime

    def getId(self):
        return self._id

    def getSpeed(self):
        return self._speed

    def getMinFloor(self):
        return self._minFloor

    def getMaxFloor(self):
        return self._maxFloor

    def gettimeForOpen(self):
        return self._openTime

    def timeForClose(self):
        return self._closeTime

    def getState(self): #
        return self.state

    def getPos(self):  #
        pass

    def goTo(self) ->bool: #
        pass

    def stop(self) ->bool:  #
        pass


    def getStartTime(self):
        return self._startTime

    def getStopTime(self):
        return self._stopTime






