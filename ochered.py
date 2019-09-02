from conftest import csf,  district_code, district_queue


def query_queue(select_params, table_name, district_code, obj):
    """
        Очередь запросов в бд.
    """
    
    dis_queries = []
    base_query = 'select {}'.format(csf.build_params_query_line(select_params))
    base_query += ' from {}'.format(table_name)
    base_query += ' where isrelevant = true'
    dis_queue = district_queue(district_code)
    zamkad = ['zamkad', 'ZelAO', 'Troitsky', 'Novomoskovsky']
    if district_code == "CAO":
        base_query += " and district like '%CAO%'"
        dis_queries.append(base_query)
    elif district_code in zamkad:
        tmp = "'{}', 'SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad'"
        base_query += " and district in ({})".format(tmp.format(district_code))
        dis_queries.append(base_query)
    else:
        base_query += " and district in ('{}', '{}')"
        for dis in dis_queue:
            dis_queries.append(base_query.format(*dis))
    spec = obj.speciality
    if spec == 'buildings_industrials_warehouses' or spec == 'buildings_offices_shoppings_free':
        return dis_queries
    queries = []
    if obj.building_type == 'жилое':
        types = ['Жилое', 'Нежилое', '']
    else:
        types = ['Нежилое', 'Жилое', '']
    for q in dis_queries:
        for typ in types:
            query = q + " and isbuildingliving = '{}'".format(typ)
            queries.append(query)
    return queries

