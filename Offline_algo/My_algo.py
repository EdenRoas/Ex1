from elevator import Elevator
from building import Building
from calls import Calls
import json
import csv

class My_algo():
    def __init__(self, buildingfile, callsfile):
        self.buildingfile = buildingfile
        self.callsfile = callsfile
        self.building = { }
        self.init_from_json_file(buildingfile)
        self.calls = []
        self.init_from_csv_file(callsfile)

    def save_to_file(self, file_name: str) -> None:
        try:
            with open(file_name, 'w', newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(header)  #*
                csvwriter.writerows(self.calls)

        except IOError as e:
            print(e)


    def init_from_csv_file(self, file_name: str):
        with open(file_name , "r") as f:
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

    def main(self) -> None:
        file_name = "Ex1_Calls"
        """if the number of elevator is 0 then dont change the file and save it as it is"""
        if self.building.numberOfElevetors == 0:
            self.save_to_file(file_name)
            return
         """if the number of elevator is 1 then change the last column of the all the calls to 0,
                meaning send all the calls to elevator 0 and then save the array of calls to a new fil"""
        elif self.building.numberOfElevetors == 1:
            for call in range(len(self.calls)):
                call[6] = 0
            self.save_to_file(file_name)
            return


