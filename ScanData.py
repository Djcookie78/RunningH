#from ast import Index
from distutils.util import convert_path
from operator import index
import os
import glob
import pandas as pd
import time

start_time = time.time()

# create class for scanning files
class ScanFiles:
    def __init__(self, csvpath):
        self.csvpath = csvpath        

    def run(self):
        self.getpaths(self.csvpath)
        self.csvpath = self.pathParser(self.csvpath)
        self.GetData()
       
    def getpaths(self, ScanInput):
        print("Scanning ", ScanInput)
        # read csv file
        df = pd.read_csv(ScanInput)
        # Dataframe replace \ with \\ in rows where header "Path"
        df['Path'] = df['Path'].str.replace("\\", "\\\\", regex=True)
        self.df = df

    def pathParser(self, path):
        # change backslash to doubble backslash
        converted_path = path.replace("\\", "\\\\")
        return converted_path

    def GetData(self):
        #print((self.df['Dyno']))
        for ind in self.df.index:
            #print(self.df['Dyno'][ind], self.df['Path'][ind])
            #print('\n\n')
            os.chdir(self.df['Path'][ind])
            for file in glob.glob("*.xls"):
                # read xls file if sheet name is "CustomModalTestData"
                try:
                    print("Reading " + file)
                    df = pd.read_excel(file, sheet_name="CustomModalTestData")
                except:
                    print("No CustomModalTestData sheet in " + file)
                continue
            # if DynoSpeed does not exist in the sheet, skip the file
            if "DynoSpeed" not in df.columns:
                continue

            # if exists rename column "Time.1 [Date]" to "Time [Date]"
            if "Time.1 [Date]" in df.columns:
                df = df.rename(columns={"Time.1 [Date]": "Time [Date]"})
            
            


            

            
        
        


# set root path with variable and change \ to \\

#csvPath = add.slash"C:\Users\BLA\OneDrive - Dinex Group\Python\RunningH\RunningH\ScanInput.csv"

csvpath = r"C:\Users\BLA\OneDrive - Dinex Group\Python\RunningH\RunningH\ScanInput.csv"

ScanAll = ScanFiles(csvpath)
ScanAll.run()


# print time for task to complete
print("Task completed in: ", time.time() - start_time, "seconds")