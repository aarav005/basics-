 
  #classs (object oriented programming) the best 
class emplo():
    raise_amount= 1.04 # has to called using class or instance # it is a class variable
    num_of_emp= 0 # they are shared among the instances within the class

    #__init__ is used for the object oriented programming
    def __init__ (self,first, last,pay): # self is a initializer , the name can be different
        self.first= first #(.first does not have to be the same name)
        self.last = last
        self.pay = pay
        #self.email= first + '.' + last + '@compay.com'
        emplo.num_of_emp= emplo.num_of_emp+1 #emplo. used when the value is constant thorough out
    @property
    def email(self): #example for property
        return '{} .{}@email.com'.format(self.first,self.last)
    @property 
    def fullname(self): # this method is created so that the hastle of calling emp_1.first, last will eliminate
        print("the full name is" +" "+ self.first +" "+  self.last) # the use of print is reutring 'none' 
    
    #setter method in property decorater
''' @fullname.setter 
    def fullname(self,name): # this lets us set the data through the method function
        first,last =name.split(' ')
        self.first= first
        self.last=last
    #deleter example
    @fullname.deleter
    def fullname(self): #acccepts only self
        print('delete the name')    
        self.first = None
        self.last = None
emp_1= emplo('john','smith')
emp_1.first= 'jim'
#for .setter
emp_1.fullname ='corey smith' # see how the we changed emp_1 into corey smith through setter

print(emp_1.first)
print(emp_1.fullname) #see how the we are able to acccess fullname as attribute, not method
print(emp_1.email) # without uisng @property the email(inside the initilizer) is still shows john while it was changed to jim 
del emp_1.fullname''' #sets the value to none 

'''def applyraise(self):
        self.pay= (self.pay* self.raise_amount)
    def __repr__(self): # used to recreate the object,, used for logging , debugging allows ho
        return "employee{} {} {}".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} {}'.format(self.fullname(),self.email)
emp_1= emplo("corey","gory",3000)
print(repr(emp_1))
print(str(emp_1))
print(id(emplo))'''


'''#creating subclass,

class developer(emplo):
    raise_amount=1.10 #the raise amount for this particular class, by default it takes the variable of the main class
    def __init__(self,first,last,pay,prog_lang):
        #calling the main class
        super().__init__(first,last,pay) #this passes theses arguments into the class emplo and prog_lang is passed thorugh developer
        self.prog_lang = prog_lang

dev_1=developer('corey','gorey', 2000,'python')



print(dev_1.email)
print(dev_1.prog_lang)'''

# important function issubclass(), isinstance()

'''#using class method

    @classmethod #this takes class as the first argument
    def set_raise_amt(cls,amount):#cls is the calss variable 
        cls.raise_amount = amount 

    #using class as alternative constructor #  the string is passed and yet we are able to add the employee into the class
    @classmethod
    def add_new_emplo(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday==6:
            return False
        else:
            return True
 #example for static method           
import datetime
mydate=datetime.date(2016,7,11)
print(emplo.is_weekday(mydate))


   
    
 #example for class variable and class method      
emplo.set_raise_amt(1.0555) # this changes the class variable raise_amount to 1.0005 from 1.4 which applies to all instances
    
        
emp_1 = emplo('corey', 'borey', 70000)

emp_2 = emplo('aarav', 'rana', 10000000000)
emp_str_1='john-doe-30000' #for class method
new_emp_1= emplo.add_new_emplo(emp_str_1) #for class method



#print(emp_1.fullname()) 
#print(emplo.fullname(emp_1))# passses emp_1 as the self # does the same thing as emp_1.fullname()
#print(emp_1.__dict__)
#emp_1.raise_amount= 1.5  #it chages the varible raise_amount for emp_1
#print(emp_1.pay)
#emp_1.applyraise()
#print(emp_1.pay)

print(emp_2.first)
print(emplo.num_of_emp)
print(emp_2.raise_amount)
print(emplo.raise_amount)
print(new_emp_1.first)'''
    


