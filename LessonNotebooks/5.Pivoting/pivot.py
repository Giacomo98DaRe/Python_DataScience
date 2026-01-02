import pandas as pd
import numpy as np
from utilities.reader_tools import GenericDatasetReader

def Pivoting(df_gdp: pd.DataFrame):
    
    # Reshape data with pivoting
    reshaped_gdp = df_gdp.pivot(index="year", columns="country", values="gdppc")
    print(reshaped_gdp)
    
    return

def Pivoting_table(supermarket_df: pd.DataFrame):
    
    # We select only numeric types (int, float) plus the index column (common pattern in Machine Learning pipelines)
    # numeric_cols = supermarket_df.select_dtypes(include=[np.number]).columns.tolist()
    # print("Numerical columns: ", numeric_cols)
    # reshaped_supermarket = supermarket_df.pivot_table(
    #     index="Gender",
    #     values=numeric_cols,
    #     aggfunc="sum"
    # )
    
    reshaped_supermarket = supermarket_df.pivot_table(
        index="Gender",
        columns="Product line",
        values=["Quantity", "Total"],
        aggfunc="sum"
    )
    print(reshaped_supermarket)
    
    return

if __name__ == "__main__":
    
    df_gdp = GenericDatasetReader.DataframeFromCSV("gdp.csv", encoding="cp1252")
    supermarket_df = GenericDatasetReader.DataframeFromExcel("supermarket_sales.xlsx")
    # Since I'm in a project environment, I have to specify the print function to display the .head() in the terminal 
    # I can add this options to better display the results
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', 1000)
    
    # print(df_gdp.head())
    print(supermarket_df.head())
    
    # Pivot method
    # Pivoting(df_gdp)
    
    # Pivot table method. It is a pivoting method with aggregation
    Pivoting_table(supermarket_df)