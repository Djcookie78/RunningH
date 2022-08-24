import os
import glob
import pandas as pd
import time

start_time = time.time()

path_root = "C:/Users/BLA/OneDrive - Dinex Group/Python/RunningH/"

# create class for collecting data from files
class CollectRes:
    def __init__(self):
        #self.inputfile = inputfile
        self.columns=["File","Time [Date]","ActDynoOperatingHours [Real]","DynoSpeed [rev/min]","DynoTorque [Nm]","Power [kW]","max_power [kW]","max_ActDynoOperatingHours [Real]","Dyno"]
        self.df_all = pd.DataFrame(columns=self.columns, index=None)  


    def read_csv(self, path):
        # read csv file
        df = pd.read_csv(path, header=None)
        # add column names to dataframe
        df.columns = self.columns
        self.append_df(df)
    

    def append_df(self, df):
        #self.df_all.concat(df)
        # join two dataframes
        self.df_all = self.df_all.append(df)


    def run(self, path_root):
        os.chdir(path_root)
        for file in glob.glob("*.csv"):
            print(file)
            self.read_csv(file)
            # print(Out.read_csv())
            # save out.read to a new directory
        self.df_all.reset_index(drop=True, inplace=True)




readdataclass = CollectRes()
readdataclass.run(path_root)
df = readdataclass.df_all
#print(df)
# write to excel file where runninghours is equal to 300
df_T250 = df[df['Dyno'] == "T250"]
# sort df_T250 by date
df_T250 = df_T250.sort_values(by=['Time [Date]'])
df_T250.to_excel("C:/Users/BLA/OneDrive - Dinex Group/Python/outputT250.xlsx", index=False)

#sdffsf
    


# print time for task to complete
print("Task completed in: ", time.time() - start_time, "seconds")