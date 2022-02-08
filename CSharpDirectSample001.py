import MATApiLib

print('CSharpDirectSample001')

a = 2
b = 1
ret = MATApiLib.MAT_CSharp_Plus(a, b)
print(a , '+', b,  ' = ', ret)

ret = MATApiLib.MAT_CSharp_Hello("kim bong seok")
print(ret)

print('test finished!')