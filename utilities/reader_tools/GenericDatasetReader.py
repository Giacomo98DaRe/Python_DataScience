import os
import pandas as pd

def DataframeFromCSV(csv_name, setIndexName=None, **kwargs):
    base_path = os.path.dirname(os.path.abspath(__file__))

    os.getcwd()
    csv_path = os.path.normpath(os.path.join(base_path, "..", "..", "data", csv_name))

    df = pd.read_csv(csv_path, **kwargs)
    
    if(setIndexName):
        df.set_index(setIndexName, inplace=True)
        
    return df


def DataframeFromExcel(excel_name, setIndexName=None):
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    os.getcwd()
    excel_path = os.path.normpath(os.path.join(base_path, "..", "..", "data", excel_name))
    
    df = pd.read_excel(excel_path)

    if(setIndexName):
        df.set_index(setIndexName, inplace=True)        
    
    return df