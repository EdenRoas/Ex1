from Calls import calls

class elevator():
    UP = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime,_startTime, _stopTime):
        self._id = int(_id)
        self._speed = float(_speed)
        self._minFloor = int(_minFloor)
        self._maxFloor = int(_maxFloor)
        self._closeTime = float(_closeTime)
        self._openTime = float(_openTime)
        self._startTime = float(_startTime)
        self._stopTime = float(_stopTime)
        self._call_list = []
        self.__number_of_calls = 0
        self.pos = 0

    def UpdateListOfCalls(self, call):
        self._call_list.append(call)
        self.__number_of_calls += 1

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

    def getPos(self, accure_time):
        time_tot = 0
        index = 0
        position = 0
        while time_tot < accure_time:
            if index == self.__number_of_calls:
                break
            cl = self._call_list[index]
            position = cl.getSrc()
            floor_range = abs(cl.getDest() - cl.getSrc())
            time_tot = time_tot + self._closeTime + self._openTime + (floor_range / self._speed) + self._startTime + self._stopTime
            if (time_tot < accure_time) and (index < (self.__number_of_calls - 1)) and (time_tot + cl.get_call_time()) > self._call_list[index + 1].get_call_time():
                tmpcl = cl
                index_of_tmpcl = self._call_list.index(tmpcl)
                while (self._call_list[index_of_tmpcl + 1] is not None) and (time_tot < accure_time) and\
                        ((time_tot + tmpcl.get_call_time()) > self._call_list[index_of_tmpcl + 1].get_call_time()):
                    index += 1
                    if self._call_list[index_of_tmpcl + 1].getSrc() < cl.getDest():
                        time_tot = time_tot + self._closeTime + self._openTime + self._startTime + self._stopTime
                    if self._call_list[index_of_tmpcl + 1].getDest() < cl.getDest():
                        time_tot = time_tot + self._closeTime + self._openTime + self._startTime + self._stopTime
                    tmpcl = self._call_list[index_of_tmpcl + 1]
                    index_of_tmpcl += 1
                    if index_of_tmpcl == (self.__number_of_calls - 1):
                        break
            if time_tot == accure_time:
                position = cl.getDest()
            elif time_tot > accure_time:
                time_dif = time_tot - accure_time
                num_of_floors = time_dif / self._speed
                if cl.getType() == calls.UP:
                    position = cl.getDest() - num_of_floors
                elif cl.getType() == calls.DOWN:
                    position = cl.getDest() + num_of_floors
            else:
                index += 1
        self.pos = position
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