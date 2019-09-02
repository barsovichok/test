
class csf(object):

    def build_params_query_line(self):
        smth_param = "some_param"
        return smth_param


class obj(object):

    def speciality(self):
        speciality = 'buildings_industrials_warehouses'
        return speciality

    def building_type(self):
        building_type = 'жилое'
        return building_type



def district_code():
    district_code = "ZAO"
    return district_code


def district_queue(dis_code="ZAO"):
    dis_queue = ['SAO-mkad', 'SVAO-mkad', 'VAO-mkad', 'UVAO-mkad', 'UAO-mkad', 'UZAO-mkad', 'ZAO-mkad', 'SZAO-mkad']
    dis_queue.append(dis_code)
    return dis_queue