import re

a=str(input())
b=str(input())
b = b.replace('*','.*')
if re.fullmatch(b, a):
    print('OK')
else:
    print('KO')