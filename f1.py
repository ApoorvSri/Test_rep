import openpyxl as xl
wb = xl.load_workbook("transactions")
sheet = wb["Sheet1"]
cell1 = sheet.cell(1 , 1)
print(cell1.value)
print("First commt")


