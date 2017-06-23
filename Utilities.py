#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 22, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------
import json
from pprint import pprint
import os

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

    def write_file(self, data, filename):
        try:
            os.remove(filename)
        except OSError:
            pass

        f1 = open(filename, 'a')

        f1.write("lat,lon\n")
        for p in data:
            f1.write("{0},{1}\n".format(p[0],p[1]))

    def convert_json_file(self, inputfile, outputfile):
        self.load_json_file(inputfile)
        output_data = self.parse_lat_lon_data()
        self.write_file(output_data, outputfile)