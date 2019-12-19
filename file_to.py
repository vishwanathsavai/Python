import xlsxwriter 

workbook = xlsxwriter.Workbook('hello.xlsx') 
file1 = open('sample.txt','r')
list1= []
for i in file1.readlines():
    list1.append(int(i))
print(list1)
file1.close()
worksheet = workbook.add_worksheet() 
print(list1[0])
# Use the worksheet object to write 
# data via the write() method. 
worksheet.write('A1', list1[0]) 
worksheet.write('B1', list1[1]) 
worksheet.write('C1', 'For') 
worksheet.write('D1', 'Geeks') 
  
# Finally, close the Excel file 
# via the close() method. 
workbook.close() 