class calculator:

    def add(self,a,b):
      return a+b

    def subtract(self,a,b):
       return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def divide(self,a,b):
        return a/b

#Create a calculator obbject

my_cl = calculator()

while True:
    print('1:Add')
    print('2:Subtract')
    print('3:Multiply')
    print('4:Division')

    ch = int(input('select operation: '))

#Make sure the user entered the valid choice.

    if ch in [1,2,3,4]:
#first ask the user do want to exit.
      if ch == 5:
          break
#if not then ask for the input and
#call appropriatemaethods

    a = int(input('Enter the first number:'))
    b = int(input('Enter the second number:'))

    if ch == 1:
        print(a,'+',b, '=' ,my_cl.add(a,b))
    elif ch == 2:
        print(a,'-',b, '=' ,my_cl.subtract(a,b))
    elif ch == 3:
        print(a,'*',b ,'=' ,my_cl.multiply(a,b))
    elif ch == 4:
        print(a,'/',b ,'=' ,my_cl.divide(a,b))
    break