def calculator():
    while True:
        x = int(input('Enter the number : '))
        y = int(input('Enter the number : '))
        c = int(input('''
1 ) add
2 ) sub
3 ) multi
4 ) div
    '''))
        if c==1:
            r = x + y
        elif c==2:
            r = x - y
        elif c==3:
            r = x * y
        elif c==4:
            r = x / y
        else:
            print('You Enter Wrong number')
        print('The Result : ',r)
        print('===============')

calculator()
