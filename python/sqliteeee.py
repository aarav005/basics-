import sqlite3 # this is a standard library in python
#importng the class from the same directory
from OOP import  emplo

#employee.db is either created or connected,, sqlite knows what to do with it
conn = sqlite3.connect('employees.db') # (':memory:') for inmemory databse

c = conn.cursor() # lets us execute the sql command USING. EXECUTE COMMAND
#creating a table
'''c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer
            )""")'''
#using function to add, get, update, delete

def insert_emp(emp):
    with conn: #it is a context manager, that lets us skip commit()
        c.execute("INSERT INTO employees VALUES(?,?,?)",(emp.first,emp.last,emp.pay))
def get_emps_by_name(lastname):
    #selecte statements doesnt need to be commited
    

    c.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname}),
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay= :pay
                    WHERE first= :first AND last =:last """,
                    {'first':emp.first,'last':emp.last,'pay':emp.pay})
def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first=:first and last=:last",# first form the main table is linked with the dictnary key
                  {'first':emp.first, 'last':emp.last})#dictnary key is linked with the entered value




 #operation from class
emp_1=emplo('john','doe',3000)
emp_2=emplo('jane','call',4890)

#working with function
insert_emp(emp_1)
empss=get_emps_by_name('doe')
print(empss)

conn.close()

'''#using tuples as place holder
c.execute("INSERT INTO employees VALUES(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
conn.commit()
#using dictnaries
c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})
conn.commit()


#ADDING VALUE TO THE DATABASE
#c.execute("INSERT INTO employees VALUES('COREY','SCHAFER',50000)")


#QUERING THE DATABASE TO SEE THE VALUES INSIDE IT
#select can be executed using tuple or dict method like above
c.execute("SELECT * FROM employees WHERE last= 'doe'")
#c.execute("SELECT * FROM employees WHERE last=?",('doe',)) tuple
#c.execute("SELECT * FROM employees WHERE last=last",{last:'doe'})

#fetching the values
print(c.fetchone())
conn.commit()
conn.close()'''












