import xlsxwriter 
name = input("Give file to be used with location if needed : ")
file1 = open(name,'r')
list1= []
for i in file1.readlines():
    list1.append(int(i))
print(list1)
file1.close()




name1 = input("Give standard excel file name with extension to be writed to : ")

workbook = xlsxwriter.Workbook(name1) 
worksheet = workbook.add_worksheet()

row = 0
column = 0
for i in list1:
    worksheet.write(row,column,i)
    row+=1
workbook.close() 