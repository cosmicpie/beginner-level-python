def get_number():
    while True:
       n = input("enter number here:-").strip()

       if n == "":
        print("please enter an number")
        continue
       
       try: 

        number = (int(n))
        return number
       
       except ValueError:
         print("please enter number only!!")
         continue

      
def is_even(number):
  if number % 2 == 0 :
    return "even"
  else:
    return "odd"

def is_prime(number):

  for i in range(2,number):
    if i % number == 0:
      return " not prime"

  else:
    return "its prime"

def factorial(number):
  f=1
  for i in range(1,number+1):
     f = f*i
  return f

def digit_sum(number):
  result =0 
  while number > 0:
    digit = number%10
    result = result+digit
    number = number//10
  return result

def total(a,b,c,d,number):
  print(f"even/odd:-  {number} is  {a} number")
  print(F"prime:-     {number} is  {b} number")
  print(f"factorial:- {number} is  {c}")
  print(f"digit sum:- {number} is  {d}")

def main():
  while True:
    number = get_number()
    a = is_even(number)
    b = is_prime(number)
    c = factorial(number)
    d = digit_sum(number)
    total(a,b,c,d,number)
    per = input("do you want to try again(y/n)").strip().lower()
    if per == "y":
      continue
    else:
      break

main()