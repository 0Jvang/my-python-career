from pyecharts import Geo
from DealData import get_city_list
from collections import Counter

c = get_city_list()
c = Counter(c)
attr = list(c.keys())
value = list(c.values())
geo = Geo('职位地理分布', width = 1200, height = 600, title_pos = 'center',title_color = 'white', background_color="#404a59")
geo.add('', attr, value, type = 'scatter', maptype = 'china',symbol_size = 10, visual_range=[0, 200], is_visualmap=True\
	, border_color = 'white')
geo.render()
