

#user se operation leta hai
def get_operation():
   while True:
    
    print("""
          chose the operation you wanna perform
          addition : ('+')
          subtraction : ('-')
          multiplication ; ('*')
          division : ('/')
          """)
    operation = input('enter operation here:-').lower().strip()

    if operation in {"*","-","+","/"}:
     return operation 
    
    else:
       print("please select operation carefully!!!!!!!!")
       continue

#user se numbers leta hai
def get_numbers(operation):
    while True:
     
     print('enter numbers seprated by space( ).')
     n = input("enter here :-")
   
     nums = n.split()

     if n.strip() == "":
        print("please enter numbers")
        continue
     
     try:

      numbers =[float(i) for i in nums]

      if operation in ["*","/"] and len(numbers) < 2:
         print("cant divide or subtract a single number please enter too or more!!")
         continue

      if operation == '/' and 0 in numbers[1:]:
        print("division by zero is not possible please try again !!!! ")
        continue

      return numbers
     
     except ValueError:
        print("please enter numbers only")
        continue

 # main calculation logic   
def calculation(operation,numbers):

     # addition logic\\\\-----------------
     if operation == '+':
        add = sum(numbers)
        return add 
    
    #subtraction logic \\\\\\\---------
     elif operation == '-':
        sub = numbers[0]
        for i in numbers[1:]:
           sub -=i
        return sub


    # multiplication logic\\\\\\\\\\\\--------------
     elif operation == '*':
        mul = 1
        for i in numbers:
            mul *= i 
        return mul
     
    # division logic//Error handeling\\\\\\\\\---------
     elif operation == '/':
        div = numbers[0]  
        for i in numbers[1:]:
         div /= i
        return div

#//////////main-fuction\\\\\\\\\\
def main():
    print("!!!!welcome to may calculator!!!!")
    while True:
     op = get_operation()
     num = get_numbers(op)
     answer = calculation(op,num)
     print(f"Result:-{answer}")
     con = input("do you want to continue (y/n):-").lower().strip()
     if con != "y":
         break
     
main()