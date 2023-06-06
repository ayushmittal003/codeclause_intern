import string
import random

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits     = string.digits
symbols    = string.punctuation


passlength=int(input("Enter the length of password :"))

p=[]
p.extend((upper_case))
p.extend(lower_case)
p.extend(digits)
p.extend(symbols)

random.shuffle(p)

rp="".join(p[0:passlength])

print("your random password is here: ",rp)

