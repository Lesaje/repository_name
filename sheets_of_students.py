'''
This program takes data from .xls !only .xls, not .xlsx! and outputs list of students
who didn't pass the exams (score less than 50).
Data in .xls must look something like this:
Student name      |     Score
John              |      65
Paul              |      45
'''

import xlrd
MY_FILE = 'Students.xls'
book = xlrd.open_workbook(MY_FILE)
sheets_num = book.nsheets
sh = book.sheet_by_index(0)       #we have same number rows and columns in each sheet
our_dict = {sh.cell_value(rowx=st_number, colx=0): '' for st_number in range (sh.nrows)}
for sheet_num in range(book.nsheets):
    st_number = 1
    sh = book.sheet_by_index(sheet_num)
    while (st_number < sh.nrows):
        if (sh.cell_value(rowx=st_number, colx=1) < 50):
            our_dict[sh.cell_value(rowx=st_number, colx=0)] += sh.name + '; '
        st_number += 1
for key, value in our_dict.items():
    if value != '':
        print (key, ': ', value, sep = '')
