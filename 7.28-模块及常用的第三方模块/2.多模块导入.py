# 同时导入多个,若有相同名称功能，后导入的会将前面导入的覆盖，需打点调用
# from my_info import *
# from myy_info import *
# info()  # 无需模块名
# my_info.info()  # NameError: name 'my_info' is not defined

import my_info
# import myy_info
# my_info.info()
# myy_info.info()
# 需模块名
# info()  # NameError: name 'info' is not defined









