#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 22, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------
import json
from pprint import pprint


class Utilities:

    file_data = None

    def load_json_file(self, filename):
        with open(filename) as data_file:
            self.file_data = json.load(data_file)

    def parse_lat_lon_data(self):
        line_data = []
        for event in self.file_data["dataEvents"]:
            line_data.append([event["latitude"],event["longitude"]])
        return line_data

    def convert_json_file_to_csv(self, filename):
        self.load_json_file(filename)
        return self.parse_lat_lon_data()


