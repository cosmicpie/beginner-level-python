dic = []



def add_task(dic):

    task = input("enter task here: -- ").lower().strip()
    priority = input("enter priority(easy,medium,high):-").lower().strip()
    deadline = input("enter dead line:-").lower().strip()

    kaki = {"task":task,"priority":priority,"deadline":deadline,}
    dic.append(kaki)

def show_task(dic):
   if len(dic) == 0:
       print("there is no data to show")
       return

   for i , t in enumerate(dic,start=1):
    print(f"""
          {i}   task     : {t["task"]}
              priority : {t["priority"]}
              deadline : {t["deadline"]}
          """)
    

def delete_task(dic):

    if len(dic) == 0:
       print("there is no data to delete")
       return
    
    print("enter the number of the task you wanna delete")

    try:
     number = int(input("enter here:-"))
    except ValueError:
       print("please enter umbers only")
       return
    
    if number < 1 or number >len(dic):
       print("invalid number")
       print("chose from blow:")
       show_task(dic)
       return
    
    dic.pop(number-1)
    print(f'task number {number} deleted!!')
 
def main(dic):
   print("welcome to my to do list")
   while True:
      
      print("""
To add task enter:-     (1)
to show tasks enter:-   (2)
to delete tasks enter:- (3)
to exsit enter:-        (4)
            """)
      
      chek = input("enter here :--").strip()

      if chek == "1":
         add_task(dic)
         print("task added succesfully")
        
      elif chek == "2":
         show_task(dic)
         d = input("do you wanna delete any task(y/n)").lower().strip()
         if d == "y":
            delete_task(dic)
         else:
          print("okay")

         a = input("do you wanna add any task(y/n)").lower().strip()
         if a == "y":
            add_task(dic)
            print("task added succesfully")
         else: 
            print("okey")

      elif chek == "3":
         delete_task(dic)
      
      elif chek == "4":
         print("okay thanks for using have a nice day!!")
         break
      else:
         print("please enter care fully from the given numbers only")
         continue

      end = input("do you wanna continue(y/n)").lower().strip()
      if end == "y":
         continue
      else:
         break
      
main(dic)