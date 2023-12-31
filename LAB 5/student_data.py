def student_data():
    while True:
        c = int(input('''
1 ) Add Student.
2 ) Exit.
'''))
        print('-------------------------------')
        if c == 1:
            name = input('Enter The Name  : ')
            age = int(input('Enter The Age   : '))
            major = input('Enter The Major : ')
            print(f'''
Student Data :
--------------
NAME  : {name}
AGE   : {age}
MAJOR : {major}
--------------------------------
''')
        elif c==2:
            print('Exit ...')
            break
        else:
            print('Try Again')
            

student_data()