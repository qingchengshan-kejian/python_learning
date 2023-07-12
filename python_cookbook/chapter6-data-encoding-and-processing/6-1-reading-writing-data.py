import csv

# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     # 生成器（可迭代）
#     # 通过nex方法获取首行
#     headers = next(f_csv)
#     for row in f_csv:
#         # process row
#         print(row)
#
# from collections import namedtuple


# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     Row = namedtuple('Row', headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row)
#
# with open('stocks.csv') as f:
#     f_csv = csv.DictReader(f)
#     for row in f_csv:
#         print(row)


headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]

with open('stocks1.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)
