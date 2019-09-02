from conftest import queue_as_list, queue_as_string, queue_as_raw_list
from ochered import query_queue
from ochered_stubs import csf,  district_code, district_queue


def test_queue_select():
    assert queue_as_list(query_queue)[0].startswith("select") is True


def test_queue_some_param():
    assert queue_as_list(query_queue)[1] == 'some_param'


def test_queue_from():
    assert queue_as_list(query_queue)[2] == 'from'


def test_queue_db_name():
    assert queue_as_list(query_queue)[3] == 'Objects.DB'


def test_queue_list():
    assert str(type(queue_as_raw_list(query_queue))) == "<class 'list'>"


def test_queue_find_str_isrelevant():
    assert queue_as_string(query_queue).find("isrelevant = true") > -1


def test_queue_find_str_district():
    assert queue_as_string(query_queue).find("district in") > -1


def test_queue_find_str_isbuildingliving():
    assert queue_as_string(query_queue).find("isbuildingliving") > -1


def test_queue_count_str():
    assert queue_as_string(query_queue).count("and") == 2