
'''
import pandas as pd

def test_data_quality():
    df = pd.read_csv("output_data.csv")
    assert df.isnull().sum().sum() == 0  # Ensure no missing values
    assert df.duplicated().sum() == 0  # Ensure no duplicate rows

'''
