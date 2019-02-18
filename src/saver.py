from pathlib import Path
import pandas as pd

class Saver:
    def __init__(self,file_to_save):
        self.file_to_save = file_to_save
        dataframe_file = Path(file_to_save)
        if(not dataframe_file.exists()):
            dataframe = pd.DataFrame()
        else:
            dataframe = pd.read_csv(file_to_save)
        self.dataframe = dataframe

    def save_item(self,item_dictionary):
        item_serie = pd.Series(item_dictionary,index= item_dictionary.keys())
        self.dataframe = self.dataframe.append(item_serie, ignore_index=True, sort=False)

    def save_items(self,list_item_dictionary):
        # Put list in dataframe
        # Append dataframe to existing dataframe
        return None

    def to_csv(self):
        self.dataframe.to_csv(self.file_to_save)
