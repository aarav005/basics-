#example of closure 
''''def outer_function():
    message=input("enter a message")

    def inner_function():
        print(message)
    return inner_function #inner_function waiting to be executed

my_func=outer_function() # setting up a closure , outer_func= inner_func waiting to be executes
my_func() # executing the inner_func
my_func()'''
#example of decoder 
def decoratoe_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("this line is executed ")
        return original_function(*args,**kwargs)
    return wrapper_function

'''def display_func():
    print("display the message")

dec_display=decoratoe_function(display_func) #same as saying @decorator function
dec_display()'''

#@decorator function is same as saying dec_display=decoratoe_function(display_func)
@decoratoe_function
def display():
    print("display the message")

@decoratoe_function
def another(name,age):
    print("the name and age  is {},{}".format(name,age))
display()
another('Aarav',24)

#using class
'''class decorater_class(object):
    def __init__(self,original_function):
        self.original_function= original_function

    def __call__(self,*args,**kwargs): #using call method
        print("the call method executed it")
        return self.original_function(*args,**kwargs)
@decorater_class
def display():
    print("display the message")

@decorater_class
def another(name,age):
    print("the name and age  is {},{}".format(name,age))
display()
another('aarav',24)'''
    















