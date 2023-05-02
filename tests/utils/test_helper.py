from src.utils.helper import get_time

from datetime import datetime

def test_get_time():

    assert isinstance(get_time(), datetime)