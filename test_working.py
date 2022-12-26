from working import convert
import pytest

def test_AMAM():
    assert convert('9 AM to 10 AM') == '09:00 to 10:00'

def test_AMPM():
    assert convert('9 AM to 10 PM') == '09:00 to 22:00'

def test_PMAM():
    assert convert('9 PM to 10 AM') == '21:00 to 10:00'

def test_PMPM():
    assert convert('9 PM to 10 PM') == '21:00 to 22:00'

def test_to():
    with pytest.raises(ValueError):
        convert('9 PM 10 PM')

def test_range():
    with pytest.raises(ValueError):
         convert('9:60 PM to 10:60 PM')

def test_format():
    with pytest.raises(ValueError):
        convert('9AM to 10PM')