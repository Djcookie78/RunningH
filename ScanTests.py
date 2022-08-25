import os
import glob
import pandas as pd
import time

start_time = time.time()

# set root path
path_root = "C:\\1\\"

# create class for scanning files
class ScanFiles:
    def __init__(self, path_root):
        self.path_root = path_root
        
    # define function for scanning files in all subdirectories
    def scan_sub(self):
        for root, dirs, files in os.walk(self.path_root):
            for file in files:
                # if file ends with .xls or .xlsx and matches E160 in filename
                if file.endswith(".xls") or file.endswith(".xlsx") and "E160" in file:
                    # print path to file with slashes
                    print(os.path.join(root, file))
            

ScanAll = ScanFiles(path_root)
ScanAll.scan_sub()