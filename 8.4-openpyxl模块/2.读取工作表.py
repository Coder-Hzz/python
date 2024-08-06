import openpyxl
wb=openpyxl.load_workbook('景区天气.xlsx')
sheet=wb['景区天气']
lst=[]
for row in sheet.rows:
    rows=[]
    for cell in row:
        rows.append(cell.value)
    lst.append(rows)
for item in lst:
    print(item)


