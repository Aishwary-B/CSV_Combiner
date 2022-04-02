# CSV_Combiner

Created a simple utility to combine multiple csv files passed in as arguments to the script

The combiner will Throw an Exception in following cases

> Invalid input file path

> Empty file provided in input

> No input 
 
 # Project Details
 Write a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Your script should output a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). Use filename as the header for the additional column.
 
 # Example Execution


`` $python ./csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv >> combined.csv``
 
 
 
# How to run unit tests
 
 ``$python -m unittest unittest_combiner``
