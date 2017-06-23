#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 22, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import unittest
import Utilities as Util
import json
from unittest.mock import MagicMock


class UtilitiesTest(unittest.TestCase):

    def test_open_json_file(self):
        util = Util.Utilities()
        util.load_json_file("test_data.json")
        self.assertTrue(util.file_data!=None)
        self.assertTrue(len(util.file_data["dataEvents"])==3)

    def test_parse_lon_lat_data(self):
        util = Util.Utilities()
        util.load_json_file("test_data.json")
        parsed_data = util.parse_lat_lon_data()
        self.assertTrue(len(parsed_data)==3)
        self.assertTrue(parsed_data[0][0] == 39.087646484375)
        self.assertTrue(parsed_data[0][1] == -94.4664535522461)

        self.assertTrue(parsed_data[1][0] == 39.10447311401367)
        self.assertTrue(parsed_data[1][1] == -94.4247055053711)

        self.assertTrue(parsed_data[2][0] == 39.11735916137695)
        self.assertTrue(parsed_data[2][1] == -94.6497573852539)

    def test_save_file(self):
        # Read the file
        util = Util.Utilities()
        util.load_json_file("test_data.json")

        # Parse the file
        parsed_data = util.parse_lat_lon_data()

        # Save the file
        util.write_file(parsed_data,"test_data.csv")

        # Check the file
        with open("test_data.csv") as f:
            content = f.readlines()

        self.assertTrue(content[0].strip() == "lat,lon", msg="Error line 1.")
        self.assertTrue(content[1].strip() == "39.087646484375,-94.4664535522461" , msg="Error line 2.")
        self.assertTrue(content[2].strip() == "39.10447311401367,-94.4247055053711" , msg="Error line 3.")
        self.assertTrue(content[3].strip() == "39.11735916137695,-94.6497573852539", msg="Error line 4.")

    def test_all_in_one(self):
        # Convert the JSON into a CSV file
        util = Util.Utilities()

        util.convert_json_file("test_data.json", "int_test_data.csv")

        # Check the file
        with open("int_test_data.csv") as f:
            content = f.readlines()

        self.assertTrue(content[0].strip() == "lat,lon", msg="Error line 1.")
        self.assertTrue(content[1].strip() == "39.087646484375,-94.4664535522461", msg="Error line 2.")
        self.assertTrue(content[2].strip() == "39.10447311401367,-94.4247055053711", msg="Error line 3.")
        self.assertTrue(content[3].strip() == "39.11735916137695,-94.6497573852539", msg="Error line 4.")