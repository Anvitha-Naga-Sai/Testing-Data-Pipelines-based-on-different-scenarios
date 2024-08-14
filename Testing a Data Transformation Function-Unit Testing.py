'''
import pytest

def transform_data(data):
    # Example transformation function
    return [x * 2 for x in data]

def test_transform_data():
    input_data = [1, 2, 3]
    expected_output = [2, 4, 6]
    assert transform_data(input_data) == expected_output

'''
