import unittest
import error_msgs
import io
import os

from unittest.mock import patch
from csv_combiner import combinecsv

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

"""

Performing Unit tests for Csv Combiner

"""


class Testcombinecsv(unittest.TestCase):

    def test_validate_valid_input(self):
        """

        Case 1 - Checking if validate method works with correct file name or not
        
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file1.csv")]
        combiner = combinecsv()
        combiner.CHECK(input)

    def test_validate_invalid_input(self):
        """

        Case 2 - Checking if validate method works returns False with incorrect file name
        
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file1.cs")]
        combiner = combinecsv()
        with self.assertRaises(Exception) as context:
            combiner.validate(input)
            self.assertTrue(
                error_msgs.INVALID_INPUT_PATH in context.exception)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combine_files_valid_input(self, stdout):
        """

        Case 3 - Checking whether files are combined if file name and path is correct 
        
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file1.csv"), os.path.join(
            CURRENT_DIR, "test_files", "file2.csv")]
        combiner = combinecsv()
        combiner.combine(input)
        with open(os.path.join(CURRENT_DIR, "test_files", "combined.csv"), 'r') as file:
            expected = file.read()
        assert expected in stdout.getvalue()

    def test_combine_file_no_input(self):
        """

        Case 4 - Checking if when no input is given in file name 
        
        """
        input = []
        combiner = combinecsv()
        with self.assertRaises(Exception) as context:
            combiner.combine(input)

            self.assertTrue(
                error_msgs.NO_INPUT_ARGUMENTS in context.exception)

    def test_combine_file_invalid_input(self):
        """

        Case 5 - Checking when incorrect file name is given in file name 
        
        """
        input = [os.path.join(CURRENT_DIR, "test_files",
                              "file1_not_present.csv")]
        combiner = combinecsv()
        with self.assertRaises(Exception) as context:
            combiner.combine(input)
            self.assertTrue(
                error_msgs.INVALID_INPUT_PATH in context.exception)

    def test_combine_file_empty(self):
        """
        
        Case 6 - Checking error when empty file is given in file name 
        
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file3_empty.csv")]

        combiner = combinecsv()
        with self.assertRaises(Exception) as context:
            combiner.combine(input)
            self.assertTrue(
                error_msgs.EMPTY_FILE_EXCEPTION in context.exception)


if __name__ == '__main__':
    unittest.main()