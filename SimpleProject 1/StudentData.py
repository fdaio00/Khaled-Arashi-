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

# function to read data.
def read():
    f = open("first.txt", "r")
    for i in f :
        print('Name    : ',i)
        i = f.readline()
        print('Age     : ',i)
        i = f.readline()
        print('Major   : ',i)
        i = f.readline()
        print('Average : ',i)
        print('----------------------')
    f.close()


# function to search for Student data by name.
def search(n):
    f = open('first.txt','r')
    for i in f :
        if i==n+'\n':
            print('Name    : ',i)
            i = f.readline()
            print('Age     : ',i)
            i = f.readline()
            print('Major   : ',i)
            i = f.readline()
            print('Average : ',i)
            print('----------------------')
    f.close()

# function to update Student data by name.
def update(n):
    try:
        f = open("first.txt", "r")
        f2 = open('second.txt', "w")
        for i in f:
            if i==n+'\n':
                name = input('Enter the name to update : ')
                age = int(input('Enter the age to update : '))
                major = input('Enter the major to update : ')
                avg = int(input('Enter the average to update : '))
                f2.write(name+'\n')
                f.readline()
                f2.write(str(age)+'\n')
                f.readline()
                f2.write(major+'\n')
                f.readline()
                f2.write(str(avg)+'\n')
            else:
                f2.write(i)
                i = f.readline()
                f2.write(i)
                i = f.readline()
                f2.write(i)
                i = f.readline()
                f2.write(i)
        f.close()
        f2.close()
        os.remove("first.txt")
        os.rename("second.txt","first.txt")
        print('		Update Successfully ... !')
        print('----------------------')
    except:
        print('		error : ')
        print('----------------------')
        

# function to delete Student data by name.
def delete(n):
    try:
        f = open("first.txt", "r")
        f2 = open('second.txt', "w")
        for i in f:
            if i==n+'\n':
                f.readline()
                f.readline()
                f.readline()
            else:
                f2.write(i)
                i = f.readline()
                f2.write(i)
                i = f.readline()
                f2.write(i)
                i = f.readline()
                f2.write(i)
        f.close()
        f2.close()
        os.remove("first.txt")
        os.rename("second.txt","first.txt")
        print('		Deleted Successfully ... !')
        print('----------------------')
    except:
        print('		error : ')
        print('----------------------')


while True :
    c = int(input('''
1 ) Add Student.
2 ) Read Student Data.
3 ) Search.
4 ) Update Student Data.
5 ) Delete Student.
6 ) Exit.
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
        name = input('Enter the name of student : ')
        search(name)
    elif c==4:
        name = input('Enter the name : ')
        update(name)
    elif c==5:
        name = input('Enter the name : ')
        delete(name)
    elif c==6:
        print('exit....')
        break
    else:
        print('error')