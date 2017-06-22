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
        # Parse the file
        # Save the file
        # Check the file
        self.assertTrue(False)

