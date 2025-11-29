import os
import pandas as pd

def DataframeFromCSV(csv_name):
    
    os.getcwd()
    csv_path = os.path.join(os.getcwd(),"..", "..", "data", csv_name)

    df = pd.read_csv(csv_path)
    
    return df