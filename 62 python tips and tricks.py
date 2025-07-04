# 1: 
print("😍 ------------------------- 😍") 
marks = 80
if marks == 90 or marks == 80 or marks ==95:
    print("good job!")
    
# but same in short way
if 80 in [80, 90, 95]:
    print("god job!")
    
print("😍 ------------------------- 😍")
# 2:
marks = 80
if marks == 90 :
    print("good job!")
else:
    print("job")
    
# but in short
print("exellent work") if marks > 90 else print ("good job")

print("😍 ------------------------- 😍")
# 3:
list1 = [50, 30, 20, 40, 60, 70]
empty_list = []
for i in list1:
    empty_list.append(i*2)
print("using for loop ", empty_list)

x = [i*2 for i in list1]
print("using comprehension",x)

print("😍 ------------------------- 😍")
# 4:
list1 = [50, 30, 20, 40, 60, 70]
index = 0
for i in list1:
    print(index,i)
    index +=1
    
# but in short
for i in enumerate(list1):
    print(i)
    
    
print("😍 ------------------------- 😍")
# 5:  _as separators
num1 = 90_00_000
num2 = 10_000
sum1=(num1+num2)
print(f'{sum1:,}')


print("😍 ------------------------- 😍")
# 6:  lambda function
def square(x):
    return x*x
print(square(4))

# but in short
a = lambda b: b**2
print(a(4))


print("😍 ------------------------- 😍")
# 07  zip function

print("ali has scored 98 marks in math")
print("ahmed has scored 80 marks in math")
print("kashif has scored 45 marks in math")
print("akmal has scored 67 marks in math")

# but in short
names = ["ali","ahmed","kashif","akmal"]
marks = [98, 80, 50, 95]
subjects = ['math',"art","biology","psy"]
print('  ')
for name, mark, subject in zip(names, marks, subjects):
    print(name,"has scored",mark,"marks in ",subject)
    
print("😍 ------------------------- 😍")  
# 8: protect passwords in terminal
#  from getpass import getpass
# username = input("enter username:")
# pasword = input("enter password:")
print("login successful")

# 
from getpass import getpass
# username = input("enter username:")
# pasword = getpass("enter password:")
print("login successful")
#  


print("😍 ------------------------- 😍")  
# 9: sort unique values
l = [10,30,20,40,30,40,60,50,30,20]
print(l)
my_set = set(l)
print(list(my_set))



print("😍 ------------------------- 😍")  
#  10  format string with f string
name = "kami"
print("my name is ",name)
print(f'my name is {name}')


print("😍 ------------------------- 😍")  
# 11:sorted to sort the complex iterables
l1 =[67, 30, 56,28,96,12]
sorted_list = sorted(l1, reverse=True)
print(sorted_list)

# onlyfans

dl = [{"name":"rosi","marks":55},
      {"name":"joe","marks":44},
      {"name":"chandler","marks":67},
      {"name":"gunther","marks":96}]
sorted_data = (sorted(dl,key=lambda x:x["marks"]))
for i in sorted_data:
    print(i)


print("😍 ------------------------- 😍")  
#  12:

dict1 = {"name":"rosi","marks":55}
dict2 = {"name":"joe","marks":44}

md = { **dict1, **dict2}
print(md)


print("😍 ------------------------- 😍")  

# 13 unpacking using _ and * variable

a, b , *c, d = (20, 10, 30, 40, 50, 60, 70)
print(a)
print(b)
print(c)
print("😍 ------------------------- 😍")  

a, b , *_ = (20, 10, 30, 40, 50, 60, 70)
print(a)
print(b)



print("😍 ------------------------- 😍")  
# 14: generators to save the memory

import sys

l = [i for i in range(90000)]
print(sum(l))
print(sys.getsizeof(l), "bytes")  # Closing parenthesis added

# but
gen = (j for j in range(90000))
print(sum(gen))
print(sys.getsizeof(gen), "bytes")



print("😍 ------------------------- 😍")  
# 15: join to concatenate strings

l33 = ["welcome"," to ","this","course"]
aa = ""
for i in l33:
    aa+=i +" "
print(aa)

# but
aaa = " ".join(l33)
print(aaa)