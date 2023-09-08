import re
inp_email=input()
pattern = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
if re.match(pattern, inp_email):
    print('OK')
else:
    print('WRONG')