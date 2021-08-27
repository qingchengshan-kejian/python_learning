#!/usr/bin/python
# -*- coding:UTF-8 -*-

import datetime
if __name__=='__main__':
    #output the date of today, in the format dd/mm/YYYY
	print(datetime.date.today().strftime('%d/%m/%Y'))

	#create date object
	yueBirthDate=datetime.date(1941,1,5)

	print (yueBirthDate.strftime('%d/%m/%Y'))

	#the arithmetic operation of date
	yueBirthDateNextDay=yueBirthDate+datetime.timedelta(days=1)
	print (yueBirthDateNextDay.strftime('%d/%m/%Y'))

	#the replace of date
	yueFirstBirthDay=yueBirthDate.replace(year=yueBirthDate.year+1)

	print (yueFirstBirthDay.strftime('%d/%m/%Y'))