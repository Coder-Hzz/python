import pdfplumber
with pdfplumber.open('访谈报告1.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print(f'---------第{i.page_number}页---------')

