import os
import pandas as pd

def DataframeFromCSV(csv_name, encoding=None):
    
    os.getcwd()
    csv_path = os.path.join(os.getcwd(),"..", "..", "data", csv_name)
    
    if(encoding):
        df = pd.read_csv(csv_path, encoding=encoding)
    else:
        df = pd.read_csv(csv_path)
    
    return df