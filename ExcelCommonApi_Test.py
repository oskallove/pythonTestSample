import ctypes
import os
from ctypes import *

print(os.path.dirname(__file__))

dll_name = "ExcelCommonApi.dll"
scriptpath = os.path.dirname(os.path.abspath(__file__))
dllpath = os.path.abspath(os.path.join(scriptpath, os.pardir)) + os.path.sep + 'Dll' + os.path.sep + dll_name
#dllpath = dll_name

print(dllpath)

ExcelCommonApi_Dll = WinDLL(dllpath)
MAT_EXCEL_Open = ExcelCommonApi_Dll['MAT_EXCEL_Open']
MAT_EXCEL_Open.argtypes=[c_char_p]
MAT_EXCEL_Open.restype=c_int

MAT_EXCEL_SetInteger = ExcelCommonApi_Dll['MAT_EXCEL_SetInteger']
MAT_EXCEL_SetInteger.argtypes=[c_char_p, c_char_p, c_long, c_int]
MAT_EXCEL_SetInteger.restype=c_int

MAT_EXCEL_GetInteger = ExcelCommonApi_Dll['MAT_EXCEL_GetInteger']
MAT_EXCEL_GetInteger.argtypes=[c_char_p, c_char_p, c_long]
MAT_EXCEL_GetInteger.restype=c_int

MAT_EXCEL_Close = ExcelCommonApi_Dll['MAT_EXCEL_Close']
MAT_EXCEL_Close.argtypes=()

excelFilePath = scriptpath + os.path.sep + 'Test.xlsx'
b_string = excelFilePath.encode('utf-8')
MAT_EXCEL_Open(b_string)
MAT_EXCEL_SetInteger('Sheet1'.encode('utf-8'), 'B'.encode('utf-8'), 5, 15)

excelValue = MAT_EXCEL_GetInteger('Sheet1'.encode('utf-8'), 'B'.encode('utf-8'), 5)
print(excelValue)

MAT_EXCEL_Close()

