import xlrd
file_location = "C:/Users/USER/Desktop/Life/hakunamatata.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
excel_date = sheet.cell_value(1, 0)
print(excel_date)
int_excel_date = int(excel_date)

#Convertinng float value into integer for comparision purpose
import datetime, time
dateoffset = 693594
date1 = datetime.date.fromordinal(dateoffset + int_excel_date)
lakshmibdate = date1.day
print("Lakshmi's bdate:", lakshmibdate)

#Below code will check today's date and just takes today's date value
from datetime import datetime
now = datetime.now()
print(now.strftime("%d"))
todaydate = now.strftime("%d")

#Comparing today's date and dates in excel to find out whether someone bday is der
diffbetweendates = int(lakshmibdate) - int(todaydate)
if diffbetweendates == 0:
    print("Today is Lakshmi's birthday")
else:
    print("not matched")
