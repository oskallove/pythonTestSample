from MatApiLibDirect import *
import os

scriptpath = os.path.dirname(os.path.abspath(__file__))
excelFilePath = scriptpath + os.path.sep + 'Test.xlsx'

MAT_EXCEL_Open(excelFilePath.encode('utf-8'))

MAT_EXCEL_SetInteger('Sheet1'.encode('utf-8'), 'B'.encode('utf-8'), 5, 15)

excelValue = MAT_EXCEL_GetInteger('Sheet1'.encode('utf-8'), 'B'.encode('utf-8'), 5)

print(excelValue)

MAT_EXCEL_Close()