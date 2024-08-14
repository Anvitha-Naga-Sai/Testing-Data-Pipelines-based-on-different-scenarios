'''

import time
from my_pipeline import run_pipeline

def test_pipeline_performance():
    input_data = "large_data.csv"
    start_time = time.time()
    run_pipeline(input_data)
    end_time = time.time()
    assert (end_time - start_time) < 60  # Ensure the pipeline runs within 60 seconds

'''
