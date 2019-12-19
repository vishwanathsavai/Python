import xlsxwriter 

workbook = xlsxwriter.Workbook('hello.xlsx') 
file1 = open('sample.txt','r')
list1= []
for i in file1.readlines():
    list1.append(int(i))
print(list1)
file1.close()
worksheet = workbook.add_worksheet() 
# Use the worksheet object to write 
# data via the write() method. 

row = 0
column = 0
for i in list1:
    worksheet.write(row,column,i)
    row+=1
  
# Finally, close the Excel file 
# via the close() method. 
workbook.close() 