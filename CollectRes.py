from doctest import OutputChecker
import os
import glob
import pandas as pd
import time

start_time = time.time()

# create class for collecting data from files
class CollectRes:
    def __init__(self, inputfile):
        self.inputfile = inputfile
        
    def read_csv(self):
        # read csv file
        df = pd.read_csv(self.inputfile)
        return df


os.chdir("C:/Users/BLA/OneDrive - Dinex Group/Python/RunningH/")
for file in glob.glob("*.csv"):
    Out = CollectRes(file)
    print(Out.read_csv())
    


# print time for task to complete
print("Task completed in: ", time.time() - start_time, "seconds")