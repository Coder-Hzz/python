import weather
import openpyxl
html=weather.get_html()
lst=weather.parse_html(html)

# 创建工作薄
workb=openpyxl.Workbook()
# 创建工作表
sheet=workb.create_sheet('景区天气')
for item in lst:
    sheet.append(item)

workb.save('景区天气.xlsx')

