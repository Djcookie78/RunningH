#scan path for xls files and run them trough function
import os
import glob
import pandas as pd
import time

start_time = time.time()

# scan path for xls files
os.chdir("C:/1")
for file in glob.glob("*.xls"):
    # read xls file if sheet name is "CustomModalTestData"
    df = pd.read_excel(file, sheet_name="CustomModalTestData")

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
    df['min_ActDynoOperatingHours [Real]'] = df['ActDynoOperatingHours [Real]'].min()

    # find highest actdynooperatinghours
    df['max_ActDynoOperatingHours [Real]'] = df['ActDynoOperatingHours [Real]'].max()

    # add file name to new column first column
    df.insert(0, 'File', file)
    
    print(df)
    # append to csv file write header only on first run
    if file == "E112-01.xls":
        df.to_csv("OUT.csv", index=False)
    else:
        df.to_csv("OUT.csv", mode='a', header=False, index=False)


# read csv file
df = pd.read_csv("OUT.csv")

# sort by date
df = df.sort_values(by=['Time [Date]'])

# write to excel file
df.to_excel("OUT.xlsx", sheet_name="running_hours", index=False)

# print time for task to complete
print("Task completed in: ", time.time() - start_time, "seconds")

print("Done")