import pytest
from ochered import query_queue
from ochered_stubs import csf,  district_code, district_queue, obj


def queue_as_list(query_queue):
    test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
    test_queue = test_queue[0]
    test_queue = test_queue.split(' ')
    return test_queue


def queue_as_raw_list(query_queue):
    test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
    return test_queue


def queue_as_string(query_queue):
    test_queue = query_queue(select_params=1, table_name="Objects.DB", district_code=['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'], obj=obj)
    test_queue_list = test_queue[0]
    return test_queue_list
