import xlrd

'''
def open_file(path):
    value = input()
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for row_num in range(sheet.nrows):
        row_value = sheet.row_values(row_num)
        if row_value[1] == value:
			print(value)
			
if __name__ == "__main__":
    path = "excel.xlsx"
    while True:
        open_file(path)

'''
	
book = xlrd.open_workbook('excel.xlsx')
sheet = book.sheet_by_index(0)
while True:
	value = input()
	for row_num in range(sheet.nrows):
		row_value = sheet.row_values(row_num)
		if row_value[1] == value:
			semicolon = row_value[3].split('，')
			comma = row_value[3].split('；')
			if len(semicolon) >= len(comma):
				definition = semicolon
			else:
				definition = comma
			for i in range(len(definition)):
				print('\n')
				print("                                                               " + definition[i])
				
			print('\n\n\n')
			break
