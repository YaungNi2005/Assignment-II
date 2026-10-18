
x=int(input('Give 1st number :'))
y=int(input('Give 2nd number :'))
z=input("Give your function(+,-,*,/):")

def add(x,y):
    print('Answer :', x+y)
    
    
def mul(x,y) :
    print('Answer :' ,x*y)
    
def sub(x,y)  :
    if x>y :
        print('Answer :' ,x-y)
        
    else :
        print('Answer :' ,y-x)
        
def div(x,y)  :
    
    if y != 0 :
        print('Answer :' ,x/y)
        
    elif y == 0 :
        print('Cannot divided by zero ')
        
   
    
if z == '+' :
    add(x,y)
    
elif z == '*' :
   mul(x,y)    
   
elif z == '-' :
   sub(x,y)
   
elif z == '/' :
   div(x,y)
    
