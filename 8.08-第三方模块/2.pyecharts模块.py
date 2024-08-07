# 1.复制代码  2.修改数据  3.运行
# 饼图
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
lst=[['bike',20],['王大锤',18],['小白',22],['小罗',12]]
c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("", lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="人物占比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("Bike.html")
)
# print([list(z) for z in zip(Faker.choose(), Faker.values())])



# 环形图
# from pyecharts import options as opts
# from pyecharts.charts import Pie
# from pyecharts.faker import Faker
# lst=[['bike',20],['王大锤',18],['小白',22],['小罗',12]]
# c = (
#     Pie()
#     .add(
#         "",
#         lst,
#         radius=["40%", "55%"],
#         label_opts=opts.LabelOpts(
#             position="outside",
#             formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
#             background_color="#eee",
#             border_color="#aaa",
#             border_width=1,
#             border_radius=4,
#             rich={
#                 "a": {"color": "#999", "lineHeight": 22, "align": "center"},
#                 "abg": {
#                     "backgroundColor": "#e3e3e3",
#                     "width": "100%",
#                     "align": "right",
#                     "height": 22,
#                     "borderRadius": [4, 4, 0, 0],
#                 },
#                 "hr": {
#                     "borderColor": "#aaa",
#                     "width": "100%",
#                     "borderWidth": 0.5,
#                     "height": 0,
#                 },
#                 "b": {"fontSize": 16, "lineHeight": 33},
#                 "per": {
#                     "color": "#eee",
#                     "backgroundColor": "#334455",
#                     "padding": [2, 4],
#                     "borderRadius": 2,
#                 },
#             },
#         ),
#     )
#     .set_global_opts(title_opts=opts.TitleOpts(title="Bike2"))
#     .render("Bike2.html")
# )
