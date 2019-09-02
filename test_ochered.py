from ochered import query_queue
from conftest import obj


def test_queue():
    test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
    assert str(type(test_queue)) == "<class 'list'>"
    test_queue = test_queue[0]
    assert test_queue.find("isrelevant = true") > -1
    assert test_queue.find("isbuildingliving") > -1
    assert test_queue.find("district in") > -1
    test_queue = test_queue.split(' ')
    assert test_queue[0].startswith("select") is True
    assert test_queue[1] == 'some_param'
    assert test_queue[2] == 'from'
    assert test_queue[3] == 'Objects.DB'
    assert test_queue.count("and") == 3