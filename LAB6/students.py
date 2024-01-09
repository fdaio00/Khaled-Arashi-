import os

# function to insert data.
def add(name , age , major , avg):        
    try:
        f = open("first.txt", "a")
        f.write(name+'\n')
        f.write(str(age)+'\n')
        f.write(major+'\n')
        f.write(str(avg)+'\n')
        print('		Added Successfully ... !')
        print('----------------------')
        f.close()
    except :
        print('		error')
        print('----------------------')

# function to update data.
def read():
    f = open("first.txt", "r")
    for i in f :
        f2.write(i)
        print('Name    : ',i)
        i = f.readline()
        f2.write(i)
        print('Age     : ',i)
        i = f.readline()
        f2.write(i)
        print('Major   : ',i)
        i = f.readline()
        f2.write(i)
        print('Average : ',i)
        print('----------------------')
    f.close()


while True :
    c = int(input('''
1 ) Add Student.
2 ) Read Student Data.
3 ) Search.
4 ) Update Data.
5 ) exit.
'''))
    print('===============================')
    if c==1:
        name = input('Enter the name : ')
        age = int(input('Enter the age : '))
        major = input('Enter the major : ')
        avg = int(input('Enter the average : '))
        add(name,age,major,avg)
    elif c==2:
        read()
    elif c==3:
#         name = input('Enter the name : ')
        search('khaled s al-arashi')
    elif c==4:
        update('khaled jalal al-arashi')
    elif c==5:
        print('exit....')
        break