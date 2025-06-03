# name=str(input("What’s your name? ")) 
# age =int(input("How old are you? ")) 
# print(f"Hello, {name}! You are {age} years old.")


# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number : "))
# if a>b:
#      a+=10
#      print("Updated number : ",a)
# else:
#      a-=5
#      print("Updated number : ",a)


# name=str(input("What’s your name? ")) 
# age =int(input("How old are you? ")) 
# fav_num=int(input("What's your favorite number? "))
# print(f"Hello {name}, You are {age} years old. Your favorite number is {fav_num}.")


# score=int(input("Enter your score : "))
# if(score<=100 and score>-1):
#     if(score<=100 and score>=90):
#         print("A+")
#         if(score>=95 and score<=100):
#             print("Congratulations on achieving HIGH DISTINcTION")
#     if(score<=89 and score>=80):
#         print("B+")
#     if(score<=79 and score>=70):
#         print("B")  
#     if(score<=69 and score>=60):
#         print("C+")
#     if(score<60):
#         print("you failed")    
# else:
#     print("invalid score")


# a=int(input("Enter the number : "))
# if a>0:
#     print("The number is positive")
# elif a==0:
#         print("The number is zero")
# else:
#     print("The number is negative")        

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum) 


# a=[4,37,82,44,98,77,13]
# for num in a:
#     if num%2==0:
#         print(num)    


# list=["Chocolate","Cake","Shake","Brownie","Ice craem"]
# for i in list:
#     print(f"I love eating {i}.")

# string="Python Programming is fun"
# vowels="aeiouAEIOU"
# v_list=[]
# for i in string:
#     if i in vowels:
#      v_list.append(i)
# print(v_list)


# list=[1,2,3,4,5,6,7,8,9,10]
# squares= [x ** 2 for x in list]
# print(squares)

# a=[]
# for i in range(1,21):
#     if i%2==0:
#         a.append(i)
# print(a)               



# for i in range(1,6):
#     for j in range(1,11):
#         print(j,"x",i,"=",i*j)
#     print()    


# days=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
# print(days[0])
# week=days[0:5]
# print(week)
# index=days.index("wednesday")
# print(index)


# string="python programming"
# print(string[0],string[-1])


# string="aiswarya"
# rev=""
# for i in string:
#     rev=i+rev
# print(rev)    


# string="aiswarya"
# print(string.count("a"))


# string="Aiswarya E S"
# print(string.replace(' ','_'))


# string="malayalam"
# print(string==string[::-1])


# set1={1,2,3,4,5,6}
# set2={2,4,6,}
# #union
# print(set1|set2)
# #intersection
# print(set1&set2)
# #difference
# print(set1-set2)
#subset or not
# print(set2<=set1)


# name=["alice","raju","riya","helen"]
# score=[70,89,50,99]
# a=zip(name,score)
# print(dict(a))
