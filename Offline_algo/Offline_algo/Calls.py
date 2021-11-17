import Elevator

class calls():
    INIT = 0
    GOING2SRC = 1
    GOIND2DEST = 2
    DONE = 3
    UP = 1
    DOWN = -1

    def __init__(self, _callTime, _src, _dest):
        self._callTime = _callTime
        self._src = _src
        self._dest = _dest
        self._assignedEle

    def getState(self):
        """returns this call current state"""
        

   # def getTime(self,state):
    #    """Returns the time (in second) of the given state, if "not there yet" returns -1
     #    @param state - the int representing the state for which the time stamp is requested"""
      #  pass

    def getSrc(self):
        """@return the source floor of this elevator call was init at."""
        return self._src

    def getDest(self):
        """@return the destenation floor to which this elevator call is targeted to."""
        return self._dest

    def getType(self):
        """@return the type of this call {UP,DOWN}"""
        if self._src > self._dest:
            return self.DOWN
        return self.UP

    def setElevator(self, index):
        self._assignedEle = index

    def allocatedTo(self):
        """This methods return the index of the Elevator in the building to which this call
         was assigned to, if not yet Assigned --> return -1"""
        if self._assignedEle == None:
            return -1
        return self._assignedEle