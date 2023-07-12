import pandas

# read a csv file, skipping last line
rats = pandas.read_csv('rats.csv', skipfooter=1)

# pandas库的使用？