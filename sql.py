import sqlite3

## connection


Connection = sqlite3.connect("student.db")


## cursor to insert record , create 


cursor = Connection.cursor()

## table 

table_info = """Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)


## INSERT RECORDS

cursor.execute('''Insert Into STUDENT values ('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values ('Jason','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values ('Rahul','Data Science','B',75)''')
cursor.execute('''Insert Into STUDENT values ('Rohan','Maths','A',35)''')
cursor.execute('''Insert Into STUDENT values ('Rakesh','Science','A',40)''')
cursor.execute('''Insert Into STUDENT values ('Yash','Devops','A',60)''')



## Display all records

print("The inserted records are ")

data= cursor.execute('''Select * from STUDENT''')


for row in data:
    print(row)
    
    
    
    ## connection close
    
Connection.commit()
Connection.close()