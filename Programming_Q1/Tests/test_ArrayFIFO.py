import datetime
from unittest.mock import MagicMock

import pytest


from Programming_Q1.Entity.fifo import ArrayFIFO


@pytest.fixture()
def arrayFIFO():
    array = ArrayFIFO()
    yield array
    del array


def test__push__must_be_added(arrayFIFO):
    arrayFIFO.push('test')
    assert arrayFIFO.size() == 1


def test__pop__return_oldest_element(arrayFIFO):
    aim_element = "test_element"
    arrayFIFO.push(aim_element)
    for i in range(10):
        arrayFIFO.push(i)
    size = arrayFIFO.size()
    assert size == 11
    assert arrayFIFO.pop() == aim_element
    assert arrayFIFO.size() == 10


def get_time_mock(date: datetime.datetime):
    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = date
    return datetime_mock


def test__addition_time__return_oldest_element_date(arrayFIFO, monkeypatch):
    aim_element = "test_element"
    aim_date = datetime.datetime(2022, 4, 3, 3, 16, 44, 270108)
    other_date = datetime.datetime(2022, 1, 1, 1, 1, 1, 0)

    monkeypatch.setattr(datetime, "datetime", get_time_mock(aim_date))

    arrayFIFO.push(aim_element)

    monkeypatch.setattr(datetime, "datetime", get_time_mock(other_date))

    for i in range(10):
        arrayFIFO.push(i)
    size = arrayFIFO.size()
    assert size == 11
    assert arrayFIFO.addition_time(aim_element) == aim_date
    assert arrayFIFO.addition_time(4) == other_date


def test__size__return_array_size(arrayFIFO):
    total_elements = 10
    for i in range(total_elements):
        arrayFIFO.push(i)
    assert arrayFIFO.size() == total_elements


def test__pop__rise_exception(arrayFIFO):
    with pytest.raises(IndexError) as exc_info:
        arrayFIFO.pop()
    assert str(exc_info.value) == 'There was an error: pop from empty list'


def test__addition_time__return_datetime_format(arrayFIFO):
    arrayFIFO.push(1)
    assert arrayFIFO.addition_time() is not None
    assert type(arrayFIFO.addition_time()) == datetime.datetime


def test__addition_time__raise_exception(arrayFIFO):
    element = 'test'
    other_element = 'abracadabra'
    arrayFIFO.push(element)
    with pytest.raises(ValueError):
        arrayFIFO.addition_time(other_element)


def test__addition_time__raise_exception_when_empty_array(arrayFIFO):
    other_element = 'abracadabra'
    with pytest.raises(ValueError):
        arrayFIFO.addition_time(other_element)
