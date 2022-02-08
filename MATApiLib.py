import ctypes
import os
from ctypes import *
import json
import ApiCommLib

comm = ApiCommLib.ApiComm('localhost', 3030)

def MAT_CSharp_Plus(a , b):
    json = ApiCommLib.JsonFunction("MAT_CSharp_Plus")
    json.addParameter("a", a)
    json.addParameter("b", b)
    comm.senddata(json.getBytes())
    ret = comm.recvdata()
    ret = int.from_bytes(ret, byteorder='little')
    return ret

def MAT_CSharp_Hello(person_name : str):
    json = ApiCommLib.JsonFunction("MAT_CSharp_Hello")
    json.addParameter("person_name", person_name)
    comm.senddata(json.getBytes())
    ret = comm.recvdata()
    ret = ret.decode('unicode_escape')
    return ret
