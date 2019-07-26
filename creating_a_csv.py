import pandas as pd
import numpy as np

class single_dataframe:
  def __init__(self):
    self.filename = ""
    self.spreadsheet = pd.DataFrame()
    self.output = pd.DataFrame()
    self.skipped_rows = 0
    self.file_path = ""

  def __read_csv(self, filename):
    print("reading", filename)
    dat = pd.read_csv(filename)
    #for index, row in dat.iterrows():
      #if (row[0] != "TIME"):
        #self.skipped_rows = index + 1
      #else:
    return pd.read_csv(filename)


  def process_csv(self, filename):
    dat = self.__read_csv(filename)
    self.file_name = filename
    self.spreadsheet = dat
    dat.drop(dat.tail(1).index, inplace=True)
    dat = pd.melt(dat, id_vars=['TIME'], var_name=["REAL 1"],value_name=" value")
    #self.file_name = self.__filter_file_name(filename)
    dat["Filename"] = self.file_name
    dat["Reference"] = dat.index
    dat["Date"] = filename[26:33]
    dat["Chip Number"] = filename[20:22]
    dat["Device Number"] = filename[23:25]
    dat["Frequency"] = np.nan

    flist = [1,251]
    for i in flist:
      if len(flist) < 841:
        a = flist[0]+flist[1]
        nextvalue = flist[-1]+a
        flist.append(nextvalue)
        nextvalue +=1

    flistnumber = [10,32,54,76,98]
    iteratetimes = 168
    flistnumber_end = flistnumber * iteratetimes

    n = 0
    m = 0
    for n in flistnumber_end:
      for m in flist:
        dat["Frequency"].iloc[flist[m]:flist[m+1]] = flistnumber_end[n]
        n +=1
        m +=1

    print(len(flist))
    print(flist)
    print(dat.tail()) #212602
    dat["Frequency"].iloc[flist[0]:flist[1]] = flistnumber_end[0]
    dat["Frequency"].iloc[flist[1]:flist[2]] = flistnumber_end[1]
    dat["Frequency"].iloc[flist[2]:flist[3]] = flistnumber_end[2]
    dat["Frequency"].iloc[flist[3]:flist[4]] = flistnumber_end[3]
    dat["Frequency"].iloc[flist[4]:flist[5]] = flistnumber_end[4]
    self.spreadsheet = dat
    self.output = self.spreadsheet

    #mask1 = dat['value'].isna()
    #groups = dat.output.loc[mask1].index
    #print(groups)



    return self


dat= single_dataframe()
dat.process_csv("/Users/ryan/Desktop/D1_C1_6.20.19_freqSweep_1-cell_edited.csv")

print(dat.spreadsheet.head())
#then when you are done modifying the dataframe this code will write it to a csv
dat.output.to_csv(r'/Users/ryan/Desktop/ryan_generated.csv')
print(len(dat.output))
#class modified:
#  def __init__(self):
#    self.file = single_dataframe()

 # def getindex(self):
  #  mask1 = self.file['value'].isna()
   # groups = self.file.output.loc[mask1].index
   # print(groups)

#dat.output = modified()
#dat.output.getindex()