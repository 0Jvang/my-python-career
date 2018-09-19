from DealData import get_education_dict
from pyecharts import Pie

e = get_education_dict()
attr = list(e.keys())
value = list(e.values())
pie = Pie('学历要求', width = 1000, height = 500)
pie.add('', attr, value, is_label_show=True, is_more_utils = True)
pie.render()
