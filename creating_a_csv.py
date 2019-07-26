import pandas as pd
import numpy as np
import os

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
    dat.drop(dat.tail(1).index, inplace=True)
    
    splicers = [-1] + np.where(np.isnan(dat.iloc[:,0]))[0].tolist() + [dat.shape[0]]
    #return splicers
    
    dat_clean = None
    for i in range(len(splicers) - 1):
        key = dat.iloc[splicers[i] + 1,0] 
        dat_block = dat\
            .iloc[splicers[i] + 2 : splicers[i + 1],]\
            .assign(
                Frequency = key,
                Reference = [x+1 for x in list(range(splicers[i + 1] - splicers[i] - 2))]
            )
        if dat_clean is None:
            dat_clean = dat_block
        else:
            dat_clean = pd.concat([dat_clean, dat_block], axis = 0)
    
    dat_clean = pd.melt(
        dat_clean, id_vars=['TIME', "Frequency", "Reference"],
        var_name=["Identifier"],value_name=" value"
    )
    #self.file_name = self.__filter_file_name(filename)
    filename = os.path.split(filename)[-1]
    dat_clean["Filename"] = self.file_name
    #dat_clean["Reference"] = dat_clean.index
    dat_clean["Date"] = filename[26:33]
    dat_clean["Chip Number"] = filename[20:22]
    dat_clean["Device Number"] = filename[23:25]
    self.spreadsheet = dat_clean
    self.output = self.spreadsheet
    
    return self


if __name__ == "__main__":
  dat= single_dataframe()
  dat.process_csv("D1_C1_6.20.19_freqSweep_1-cell_edited.csv")

  print(dat.spreadsheet.head())
  #then when you are done modifying the dataframe this code will write it to a csv
  # dat.output.to_csv(r'ryan_generated.csv')
  # print(len(dat.output))
  #class modified:
  #  def __init__(self):
  #    self.file = single_dataframe()

  # def getindex(self):
    #  mask1 = self.file['value'].isna()
    # groups = self.file.output.loc[mask1].index
    # print(groups)

  #dat.output = modified()
  #dat.output.getindex()