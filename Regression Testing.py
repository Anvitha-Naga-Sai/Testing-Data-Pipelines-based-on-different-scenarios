'''
import pytest
from my_pipeline import run_pipeline

def test_regression():
    input_data = "sample_data.csv"
    expected_output = "expected_output.csv"
    result = run_pipeline(input_data)
    assert result == expected_output  # Ensure the output remains consistent

'''
