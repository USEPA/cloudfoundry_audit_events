import openpyxl
import sys

#Passing bash script argument to python script
print ('Second script argument, passing $CF_ORG: ', sys.argv[1])
print ('Third script argument, passing $YYYYMM: ', sys.argv[2])

path = "./AuditReport-2022-04.xlsx"
wb = openpyxl.load_workbook(path.strip())
sheetlist = wb.sheetnames

# All Events - sheet1
sheet1 = wb[sheetlist[0]]

# User Access Changes - sheet2
sheet2 = wb[sheetlist[1]]

# Route Changes - sheet3
sheet3 = wb[sheetlist[2]]

# Service Instance Events - sheet4
sheet4 = wb[sheetlist[3]]

# Service Binding Events - sheet5
sheet5 = wb[sheetlist[4]]

# Service Events - sheet6
sheet6 = wb[sheetlist[5]]

print("List of Sheet names: ", sheetlist)
print("Sheet 1: ", sheet1)
print("Max row before removal: ", sheet1.max_row)

# Cleanup All Events - sheet1
rownumber = 1
for row in sheet1.iter_rows(min_row=1, max_row=sheet1.max_row, min_col=1, max_col=sheet1.max_column, values_only=True):
    rownumber += 1
for i in range(sheet1.max_row, 1, -1):
    if sheet1.cell(row=i, column=2).value != sys.argv[1]:
        sheet1.delete_rows(i, 1)

# Cleanup User Access Changes - sheet2
rownumber = 1
for row in sheet2.iter_rows(min_row=1, max_row=sheet2.max_row, min_col=1, max_col=sheet2.max_column, values_only=True):
    rownumber += 1
for i in range(sheet2.max_row, 1, -1):
    if sheet2.cell(row=i, column=2).value != sys.argv[1]:
        sheet2.delete_rows(i, 1)

# Cleanup Route Changes - sheet3
rownumber = 1
for row in sheet3.iter_rows(min_row=1, max_row=sheet3.max_row, min_col=1, max_col=sheet3.max_column, values_only=True):
    rownumber += 1
for i in range(sheet3.max_row, 1, -1):
    if sheet3.cell(row=i, column=2).value != sys.argv[1]:
        sheet3.delete_rows(i, 1)

# Cleanup Service Instance Events - sheet4
rownumber = 1
for row in sheet4.iter_rows(min_row=1, max_row=sheet4.max_row, min_col=1, max_col=sheet4.max_column, values_only=True):
    rownumber += 1
for i in range(sheet4.max_row, 1, -1):
    if sheet4.cell(row=i, column=2).value != sys.argv[1]:
        sheet4.delete_rows(i, 1)

# Cleanup Service Binding Events - sheet5
rownumber = 1
for row in sheet5.iter_rows(min_row=1, max_row=sheet5.max_row, min_col=1, max_col=sheet5.max_column, values_only=True):
    rownumber += 1
for i in range(sheet5.max_row, 1, -1):
    if sheet5.cell(row=i, column=2).value != sys.argv[1]:
        sheet5.delete_rows(i, 1)

# Cleanup Service Events - sheet6
rownumber = 1
for row in sheet6.iter_rows(min_row=1, max_row=sheet6.max_row, min_col=1, max_col=sheet6.max_column, values_only=True):
    rownumber += 1
for i in range(sheet6.max_row, 1, -1):
    if sheet6.cell(row=i, column=2).value != sys.argv[1]:
        sheet6.delete_rows(i, 1)


print("Creating new file: mod.xlsx...")
wb.save('final-AuditReport'+str(sys.argv[2])+'.xlsx')

print("Cleanup report completed...")
