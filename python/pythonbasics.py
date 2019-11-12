#''' creates a block of comment
#dictonaries
'''phonebook={"ram":["8-225-5556","email1","heigt1"],"hari":"318-222-771"}
print("printint the dictonaries value"+phonebook['ram'][1])'''

#boolean operators
#True and False

'''hours=input(("enter if workeed more than 40 hours"))
if hours==True:
   # print("pay overtime")
else:
    #print("do not pay overtime")'''

#boolean logical operators

'''response1=input("enter if worked more than 40 hours")
response2= input("enter if you want to pay")
if (response1 and response2):
    print("yes pay over time")
else:
    print("do not pay over time")'''


#if statements
'''if 5<2 and 7>4:
    print(4+1)
elif 5!=5 or not(5)!=5:
    print(3)
else:
    print("nothing")'''

#loops

#for loops
#for number in range(20,30):
    #print(number)
'''list_for= [1,2,3,4,5]
for number in list_for:
    print(number)'''
#while loop
#counting function
'''count=2
sumfun=0
while(count>0):
    sumfun=sumfun+count
    count=count-1

print(sumfun)'''

##########exercises#####
#exercice 1suming 2
'''def sum_num(num1,num2):
    x=num1+num2
    print(x)
sum_num(10,11)'''

#exercise 2
#squaring a number
'''def square_num(num1):
    print("the square of the number is",num1**2)
square_num(10)
assert 5==5##checks if the code is right
print("the code is correct")'''

#exercise 3
#find length
'''def add_string(name):
    count=0
    for i in name:
        count=count+1
    print(count)
add_string('letter')'''

# functions with return finding the max out of 3
''''def max_number(num1,num2):
    if num1>num2:
        return(num1)
    else:
        return(num2)
def max3_num(num1,num2,num3):
    return(max_number(max_number(num1,num2),num3))
x=max3_num(2,3,5)
print(x)'''
 



        


    



