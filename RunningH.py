#scan path for xls files and run them trough function
import os
import glob
from tkinter import E
import pandas as pd
import time

start_time = time.time()
Dyno = "T250"  #T250 or D600
OutputFile = "C:/Users/BLA/OneDrive - Dinex Group/Python/RunningH/E161.csv"

# scan path for xls files
os.chdir("G:/DET/Tests/Engine Dyno Tests/2022-Q3 E161 Weichai D2i-DPF/Measurements/Stars/")
for file in glob.glob("*.xls"):
    # read xls file if sheet name is "CustomModalTestData"
    
    try:
        
        df = pd.read_excel(file, sheet_name="CustomModalTestData")
    except:
        print("No CustomModalTestData sheet in " + file)
        continue


    # if DynoSpeed does not exist in the sheet, skip the file
    if "DynoSpeed" not in df.columns:
        continue
    
    # add the first rows into column names
    df.columns = df.columns +" ["+df.iloc[0]+"]" 

    # drop the first row
    df = df.drop(df.index[0])
    
    # if exists rename column "Time.1 [Date]" to "Time [Date]"
    if "Time.1 [Date]" in df.columns:
        df = df.rename(columns={"Time.1 [Date]": "Time [Date]"})

    # Get where colums is time, ActDynoOperatingHours, DynoSpeed, DynoTorque
    df = df.loc[:,['Time [Date]','ActDynoOperatingHours [Real]', 'DynoSpeed [rev/min]', 'DynoTorque [Nm]']]
    
    # add column with power as float64
    df['Power [kW]'] = df['DynoSpeed [rev/min]'] * df['DynoTorque [Nm]'] / 9549.3

    # find highest power
    df['max_power [kW]'] = df['Power [kW]'].max()

    # reduce to first and last row
    df = df.iloc[[0]]

        # find lowest actdynooperatinghours
        # df['min_ActDynoOperatingHours [Real]'] = df['ActDynoOperatingHours [Real]'].min()

    # find highest actdynooperatinghours
    df['max_ActDynoOperatingHours [Real]'] = df['ActDynoOperatingHours [Real]'].max()

    # add dynoname
    df['Dyno'] = Dyno

    # add file name to new column first column
    df.insert(0, 'File', file)
    
    print(df)
    # append to csv file write header only on first run
    if file == "E112-01.xls":
        df.to_csv(OutputFile, index=False)
    else:
        df.to_csv(OutputFile, mode='a', header=False, index=False)


# read csv file
#df = pd.read_csv("OUT.csv")

# sort by date
#df = df.sort_values(by=['Time [Date]'])

# write to excel file
# df.to_excel("OUT.xlsx", sheet_name="running_hours", index=False)

# print time for task to complete
print("Task completed in: ", time.time() - start_time, "seconds")
