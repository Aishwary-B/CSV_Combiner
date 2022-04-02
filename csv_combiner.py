import os
import sys
import pandas as pd
import error_msgs

"""
Author - Aishwary Bodhale

csv_combiner.py - Reads the csv files and add an additional column of file name

Input - csv file name and path 

Output -csv file with additional filename column 

"""

SAMPLE_SIZE = 10**6

SEPERATOR = ","


class combinecsv:

    def CHECK(self, file_list):
        """
        CHECK FUNCTION:
        checks whether file path and file is valid
        file list - a list of all files with the specified file path
        output - returns bool True if all files and file path are correct 
        """

        for file_path in file_list:
            if not os.path.isfile(file_path):
                raise Exception(error_msgs.INVALID_INPUT_PATH)
            elif os.path.getsize(file_path) == 0:
                raise Exception(error_msgs.EMPTY_FILE_EXCEPTION)
        return True

    def combine(self, file_list):
        """
        COMBINE FUNCTION:
        Combines file content and creates new column with file name, assuming the file name and path is accurate
        file_list = returns a list of all files with file path 
        """
        if not file_list:
            raise Exception(error_msgs.NO_INPUT_ARGUMENTS)

        self.CHECK(file_list)

        header = True
        for input_file in file_list:

            for SAMPLE in pd.read_csv(input_file, sep=SEPERATOR, chunksize=SAMPLE_SIZE):
                SAMPLE["filename"] = os.path.basename(input_file)

                print(SAMPLE.to_csv(index=False, header=header),  end='')
                header = False


def main():
    combiner = combinecsv()
    combiner.combine(sys.argv[1:])


if __name__ == "__main__":
    main()