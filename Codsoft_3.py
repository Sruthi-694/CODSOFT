import random
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol='(){}[];".,/*'
number='0123456789'
all=lower+upper+symbol+number
length=8
password = ""
for _ in range(length):
    password = "".join(random.sample(all,length))
print("Password")