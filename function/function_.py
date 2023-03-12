import pandas as pd
import numpy as np


class goft_data:
    def __init__(self, outlook, temp, humidity, windy, play_goft):
        self.outlook = outlook
        self.temp = temp
        self.humidity = humidity
        self.windy = windy
        self.play_goft = play_goft
    
    def write_out(self):
        print(self.outlook,
              self.temp,
              self.humidity, 
              self.windy, 
              self.play_goft)
        
class list_goft_data:
    def __init__(self):
        self.list = []
    
    def parse_list(self):
        for item in self.list:
            item.write_out()

## data deep analyst : 4 level

def read_file(file_name):
    df = pd.read_csv(file_name +".csv")
    df.to
    return df

def processing(dataframe_input):
    for item in dataframe_input.columns:
        dataframe_input.col(item)
        dataframe_input

#main
    


if __name__== "__main__":
    processing()