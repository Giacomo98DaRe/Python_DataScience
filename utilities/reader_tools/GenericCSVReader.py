import os
import pandas as pd

def DataframeFromCSV(csv_name, encoding=None, setIndexName=None):
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    os.getcwd()
    csv_path = os.path.normpath(os.path.join(base_path, "..", "..", "data", csv_name))
    
    if(encoding):
        df = pd.read_csv(csv_path, encoding=encoding)
    else:
        df = pd.read_csv(csv_path)

    if(setIndexName):
        df.set_index(setIndexName, inplace=True)        
    
    return df