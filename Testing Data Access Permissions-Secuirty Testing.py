'''
import pytest
from my_pipeline import check_permissions

def test_data_access_permissions():
    user = "test_user"
    assert check_permissions(user) == "Access granted"

'''
