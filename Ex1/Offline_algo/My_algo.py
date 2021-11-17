from Calls import Calls
from Building import Building
from Elevator import Elevator
import json
import csv
import sys
import math


class My_algo():

    def __init__(self, buildingfile, callsfile):
        self.buildingfile = buildingfile
        self.callsfile = callsfile
        self.building = {}
        self.init_from_json_file(buildingfile)
        self.calls = []
        self.init_from_csv_file(callsfile)

    def save_to_file(self, file_name):
        try:
            with open(file_name, 'w', newline="") as file:
                csvwriter = csv.writer(file)
                # csvwriter.writerow(header)
                csvwriter.writerows(self.calls)

        except IOError as e:
            print(e)

    def init_from_csv_file(self, file_name: str):
        with open(file_name, "r") as f:
            csvreader = csv.reader(f)
            header = next(csvreader)
            rows = []
            for row in csvreader:
                rows.append(row)
        self.calls = rows

    def init_from_json_file(self, file_name: str) -> None:
        new_building_dict = {}
        with open(file_name, "r") as f:
            dict_building = json.load(f)
            for k, v in dict_building.items():
                building = Building(v)
                new_building_dict[k] = building
        self.building = new_building_dict

    def allocated(self, call):
        minTimeToArrive = sys.maxsize
        for elev in self.building._elevators:
            if elev.getstate() != call.getType():
                continue
            if elev.getstate() == Elevator.ERROR:
                continue
            if (call.getType() == Calls.UP) and (elev.getstate == Elevator.UP):
                if elev.getPos() > call.getSrc():
                    continue
            if (call.getType() == Calls.DOWN) and (elev.getstate == Elevator.DOWN):
                if elev.getPos() < call.getSrc():
                    continue
            tmpTime = self.__CalcluateTimeToArrive(elev, call.getSrc(), call)
            if tmpTime < minTimeToArrive:
                minTimeToArrive = tmpTime
                index = elev.getID
        call.setElavator(index)

    def __CalcluateTimeToArrive(self, elev, floor, call):
        diffBetweenFloors = math.abs(elev.getPos() - floor)
        arraysSet = {}
        i = 0
        cl = self.calls[i]
        while cl is not call:
            if cl[1] <= (call[1] - 20):
                break
            i += 1
            cl = self.calls[i]

        while cl is not call:
            # if cl.getState is not DONE:
            if cl[6] == elev.getID():
                if call.getTtpe() == Calls.UP:
                    if cl[2] < floor:
                        arraysSet.add(cl.getSrc())
                if cl[3] < floor:
                    arraysSet.add(cl.getDest())
                if call.getTtpe() == Calls.DOWN:
                    if cl[2] > floor:
                        arraysSet.add(cl.getSrc())
                    if cl[3] > floor:
                        arraysSet.add(cl.getDest())
            cl = self.calls[self.calls.index(cl) + 1]
        numberOfStops = len(arraysSet)
        totalTimeToOpen = numberOfStops * elev.getTimeForOpen()
        totalTimeToClose = numberOfStops * elev.getTimeForClose()
        totalTimeToStart = numberOfStops * elev.getStartTime
        totalTimeToStop = numberOfStops * elev.getStopTime
        totalTimeToPassAllFloors = diffBetweenFloors * elev.getSpeed()
        totalTimeToArrive = totalTimeToOpen + totalTimeToClose + totalTimeToPassAllFloors + totalTimeToStart + totalTimeToStop
        return totalTimeToArrive

    def updateFile(self, file_name="Ex1_Calls") -> None:
        # if the number of elevator is 0 then dont change the file and save it as it is
        if self.building.numberOfElevetors == 0:
            self.save_to_file(file_name)
            return
        # if the number of elevator is 1 then change the last column of the all the calls to 0,
        # meaning send all the calls to elevator 0 and then save the array of calls to a new fil
        elif self.building.numberOfElevetors == 1:
            for call in self.calls:
                call[6] = 0
            self.save_to_file(file_name)
            return
        for call in self.calls:
            self.allocated(call)
        for call in self.calls:
            call[6] = Calls.allocatedTo(call)
        self.save_to_file(file_name)
        return

if __name__ == "__main__":
    # fileBuilding = open("Ex1\Ex1_Building\B1.json", "r")
    # fileCall = open("Ex1\Ex1_calls\call_a.csv", "r")
    a = My_algo("C:\Users\edenr\PycharmProjects\Ex1\Ex1_Building\B1.json", "C:\Users\edenr\PycharmProjects\Ex1\Ex1_calls\Calls_a.csv")
    a.updateFile("Ex1_calls_c_1")

