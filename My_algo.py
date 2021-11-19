from Elevator import elevator
from Building import building
from Calls import calls
import json
import csv
import sys

class my_algo():

    def __init__(self, buildingfile, callsfile):
        self.buildingfile = buildingfile
        self.callsfile = callsfile
        self.buildingDict = {}
        self.buildingDict = self.init_from_json_file(buildingfile)
        self._building = building(_minFloor = self.buildingDict["_minFloor"], _maxFloor = self.buildingDict["_maxFloor"], _elevators = self.buildingDict["_elevators"])
        self.callsArray = []
        self.callsArray = self.init_from_csv_file(callsfile)

    def save_to_file(self, file_name, array_Of_Calls):
        try:
            with open(file_name, 'w', newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(array_Of_Calls[0])
                csvwriter.writerows(array_Of_Calls[1:])
        except IOError as e:
            print(e)

    def init_from_csv_file(self, file_name: str):
        with open(file_name , "r") as f:
            csvreader = csv.reader(f)
            # header = next(csvreader)
            rows = []
            for row in csvreader:
                rows.append(row)
        return rows

    def init_from_json_file(self, file_name: str) -> None:
        new_building_dict = {}
        with open(file_name, "r") as f:
            new_building_dict = json.load(f)
        return new_building_dict

    def allocated(self, call):
        choosenelev = self._building._elevators_list[0]
        minTimeToArrive = sys.maxsize
        for elev in self._building._elevators_list:
            if elev.getState() == elevator.LEVEL:
                call.setElevator(elev.getID())
                elev.UpdateListOfCalls(call)
                return
            if elev.getState() != call.getType():
                continue
            if elev.getState() == elevator.ERROR:
                continue
            if (call.getType() == calls.UP) and (elev.getState() == elevator.UP):
                if elev.getPos((float)(call.get_call_time())) > call.getSrc():
                    continue
            if (call.getType() == calls.DOWN) and (elev.getState() == elevator.DOWN):
                if elev.getPos((float)(call.get_call_time())) < call.getSrc():
                    continue
            tmpTime = self.__CalcluateTimeToArrive(elev, call.getSrc(), call)
            if tmpTime < minTimeToArrive:
                minTimeToArrive = tmpTime
                choosenelev = elev
        elevid = choosenelev.getID()
        call.setElevator(elevid)
        choosenelev.UpdateListOfCalls(call)

    def __CalcluateTimeToArrive(self, elev, floor, call):
        diffBetweenFloors = abs(elev.getPos((float)(call.get_call_time())) - floor)
        arraysSet = set()
        i = 0
        cl = self.callsArray[i]
        while (i < len(self.callsArray)) and (cl is not call):
            cl = self.callsArray[i]
            if (float)(cl[1]) <= ((float)(call.get_call_time()) - 20):
                break
            i += 1
        while (i < (len(self.callsArray) - 1)) and (cl is not call):
            #if cl.getState is not DONE:
            if cl[5] == elev.getID():
                if call.getTtpe() == calls.UP:
                    if cl[2] < floor:
                        arraysSet.add(cl[2])
                    if cl[3] < floor:
                        arraysSet.add(cl[3])
                if call.getTtpe() == calls.DOWN:
                    if cl[2] > floor:
                        arraysSet.add(cl[2])
                    if cl[3] > floor:
                        arraysSet.add(cl[3])
            i += 1
            cl = self.callsArray[i]
        numberOfStops = len(arraysSet)
        totalTimeToOpen = numberOfStops * elev.gettimeForOpen()
        totalTimeToClose = numberOfStops * elev.gettimeForClose()
        totalTimeToStart = numberOfStops * elev.getStartTime()
        totalTimeToStop = numberOfStops * elev.getStopTime()
        totalTimeToPassAllFloors = diffBetweenFloors * elev.getSpeed()
        totalTimeToArrive = totalTimeToOpen + totalTimeToClose + totalTimeToPassAllFloors + totalTimeToStart + totalTimeToStop
        return totalTimeToArrive

    def updateFile(self, file_name="Ex1_Calls") -> None:
        #if the number of elevator is 0 then dont change the file and save it as it is
        if self._building.numberOfElevetors() == 0:
            self.save_to_file(file_name, self.callsArray)
            return
        #if the number of elevator is 1 then change the last column of the all the calls to 0,
        #meaning send all the calls to elevator 0 and then save the array of calls to a new fil
        elif self._building.numberOfElevetors() == 1:
            for call in self.callsArray:
                call[5] = 0
            self.save_to_file(file_name, self.callsArray)
            return
        array_of_calls = []
        for call in self.callsArray:
            call_obj = calls(_callTime = call[1], _src = call[2], _dest = call[3])
            array_of_calls.append(call_obj)
            self.allocated(call_obj)
        index = 0
        for call in self.callsArray:
            call_obj = array_of_calls[index]
            call[5] = calls.allocatedTo(call_obj)
            index += 1
        self.save_to_file(file_name, self.callsArray)
        return
