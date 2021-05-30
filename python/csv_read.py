import pandas as pd
import numpy as np
import sys


def file_read(filename):
     data = pd.read_csv("/home/harish/Burnout_Predictor/Burnout_Prediction_Python/"+filename)
     print(data['Burn Rate'])


read_file = sys.argv[1]
file_read(read_file)
