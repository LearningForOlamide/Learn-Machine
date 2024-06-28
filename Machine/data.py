import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np


# Preprocess the data for use 
def process_mammographic_data(): 
    path_to_file  = os.path.join(os.getcwd(), "Dataset/mammographic/mammographic_masses.data")
    dataset = pd.read_csv(path_to_file,)
    dataset.columns = ["Bi_rads_asssessment","Age","Shape","Margin", "Density","Severity"]
    return dataset 


