print('three numbers below:')
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))
cal=0
while cal<5:
    print('calucuator menu')
    print('1.add')
    print('2.subtract')
    print('3.multiply')
    print('4.divide')
    print('5.exit')
    cal=int(input('enter ur choice:'))
    if cal==1:
        d=c+a
        print('sum:',d)
    elif cal==2:
        d=c-a
        print('difference:',d)
    elif cal==3:
        d=c*a
        print('product:',d)
    elif cal==4:
        d=c/a
        print('quotient:',d)
    elif cal==5:
        break
    else:
        print('INVALID CHOICE')

