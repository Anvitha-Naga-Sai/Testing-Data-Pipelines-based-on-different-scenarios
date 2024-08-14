'''
import pytest

from my_pipeline import ingest_data, store_data

def test_ingest_and_store():
    input_data = "sample_data.csv"
    ingested_data = ingest_data(input_data)
    result = store_data(ingested_data)
    assert result == "Data stored successfully"

'''
