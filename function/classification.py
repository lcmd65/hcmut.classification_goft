# Machine learning classification
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# For data manipulation and to plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

#local library
from function_ import *
from data.string_data import*

class classification():
    def __init__(self):
        self.list = []

    #fetch data
    def processing():
        Df = read_file(dataset)
        Df = Df.dropna()
        Df.Close.plot(figsize=(10,5))
        plt.ylabel("write_off")
        plt.show()
# classification data patern
# data patern for treacking thu]
# functional define


