from ochered import query_queue
from conftest import obj


def test_queue_select():
    test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
    test_queue = test_queue[0]
    test_queue = test_queue.split(' ')
    assert test_queue[0].startswith("select") is True


def test_queue_some_param():
    test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
    test_queue = test_queue[0]
    test_queue = test_queue.split(' ')
    assert test_queue[1] == 'some_param'


def test_queue_from():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     test_queue = test_queue[0]
     test_queue = test_queue.split(' ')
     assert test_queue[2] == 'from'


def test_queue_db_name():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     test_queue = test_queue[0]
     test_queue = test_queue.split(' ')
     assert test_queue[3] == 'Objects.DB'


def test_queue_list():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     assert str(type(test_queue)) == "<class 'list'>"


def test_queue_find_str_isrelevant():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     test_queue = test_queue[0]
     test_str = test_queue.find("isrelevant = true")
     assert test_str > -1


def test_queue_find_str_district():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     test_queue = test_queue[0]
     test_str = test_queue.find("district in")
     assert test_str > -1


def test_queue_find_str_isbuildingliving():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     test_queue = test_queue[0]
     test_str = test_queue.find("isbuildingliving")
     assert test_str > -1


def test_queue_count_str():
     test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
     test_queue = test_queue[0]
     test_str = test_queue.count("and")
     assert test_str == 2
