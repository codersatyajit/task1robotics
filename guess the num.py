import random
num = random.randint(1000 , 9999)
# print(num)
set1 = set(str(num))
list1 = list(str(num))
# print(set1)
# print(list1)
for i in range (10):
 num2 = int(input("enter the four digit number you guessed:"))
 set2 = set(str(num2))
# print(set2)
 list2 = list(str(num2))
# print(list2)
 if set1 | set2 == set1:
    if list1 == list2:
        print("R")
        print("you have entered the perfect num.")
    else:
        print("A")
        print("number order is not correct")
 else:
    print("W")
 print("want to give anthor try!")
