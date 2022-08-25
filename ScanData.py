from distutils.util import convert_path
import os
import glob
import pandas as pd
import time

start_time = time.time()

# create class for scanning files
class ScanFiles:
    def __init__(self):
        pass
       
    def getpaths(self, ScanInput):
        # read csv file
        df = pd.read_csv(ScanInput)
        print(df)

    def pathParser(self, path):
        # change backslash to doubble backslash
        converted_path = path[0].replace("\\", "\\\\")
        # return last element of list
        return converted_path

# set root path with variable and change \ to \\

#csvPath = add.slash"C:\Users\BLA\OneDrive - Dinex Group\Python\RunningH\RunningH\ScanInput.csv"

csvpath = r"C:\Users\BLA\OneDrive - Dinex Group\Python\RunningH\RunningH\ScanInput.csv", "utf-8"


ScanAll = ScanFiles()
csvpath = ScanAll.pathParser(csvpath)
print(csvpath)
ScanAll.getpaths(csvpath)




# print time for task to complete
print("Task completed in: ", time.time() - start_time, "seconds")