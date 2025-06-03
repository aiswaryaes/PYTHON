
# algo="regression"
# print(len(algo))
# algo="iuytry"
# print(algo[0])

# print(algo[-1])

# print(algo[0:5])

# print(algo[0:5:2])

# print(algo[::-1])

# print(algo[::])

# letters='zimba'
# print(letters*3)

# string1='abc'
# string2='def'
# print(string1+string2)

# message="GOOD MORNING"
# print(message.lower())

# message="good morning"
# print(message.upper())

# txt="I love apples,apples are my favorite fruit"
# x=txt.count("p")
# print(x)


# txt="I love apples,apples are my favorite fruit"
# print(txt.count("p"))
# message='python is a fun programming language'
# print(message.find('fun'))

# text='bat ball'
# replaced_text=text.replace('ba','ro')
# print(replaced_text)

# print(11>9)
# print(10==9)
# print(10<9)

# numbers=[1,2,3,4,5]
# print("Before append:",numbers)
# numbers.append(6)
# print("After append:",numbers)

# prime_numbers=[2,3,5]
# print("List1:",prime_numbers)
# even_numbers=[6,8,10]
# print("List2:",even_numbers)
# prime_numbers.extend(even_numbers)
# print("List after append:",prime_numbers)

# prime_numbers=[2,3,5,7]
# removed_element=prime_numbers.pop(2)
# print('Removed Element:',removed_element)
# print('Updated List:',prime_numbers)

# languages=['python','java','c++','rust','c']
# del languages[1]
# print(languages) 
# del languages[-1]
# print(languages)
# del languages[0:2]
# print(languages)

# languages=['python','c++','c','java','rust']
# languages.remove('python')
# print(languages)

# prime_numbers=[2,3,5,7,9]
# prime_numbers.reverse()
# print('Reversed List:',prime_numbers)

# list1=[2,4,6,8,10]
# l =list1*2
# print(l)

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# l=list1+list2
# print(l)

# list1=[2,4,6,8,10,12,14,16,18,20]
# a=len(list1)
# print(a)

# listl=[1,2,3,4,5]
# for i in listl:
#     print(i)

# list=['Ryan','Rohan','Amy','Yashin']   
# for i in list:
#     print(i) 

# listl=[100,200,300,400,500]
# print(100 in listl)
# print(300 in listl)
# print(700 in listl)

# listl=[100,200,300,400,500]
# print(max(listl))
# print(min(listl))

# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# intersection1=set(list1).intersection(list2)
# print(intersection1)
# # second method 
# intersection2=set(list1)&set(list2)
# print(intersection2)

# Tuple_data=(0,1,2,3,2,3,3,2)
# print(Tuple_data)

#empty tuple
# my_tuple=()
# print(my_tuple)

#nested tuple
# my_tuple=("Dog",[2,4,6],(1,3,5))
# print(my_tuple)

#indexing
# letters=("o","p","q","r","s","t")
# print(letters[0])
# print(letters[5])

#negative indexig
# letters=("o","p","q","r","s","t")
# print(letters[-1])
# print(letters[-3])

#python program to show repetition in tuples
# tuple_=("adf","jfj")
# print("original tuple is: ",tuple_)

# #repeting the tuple elements
# tuple_=tuple_*3
# print("new tuple is: ",tuple_)

#iteration through a tuple 
# languages=('physics','chemistry','biology')
# for langauage in languages:
#     print(langauage)

#check if an item exist in the tuple
# languages=('physics','chemistry','biology')
# print('python' in languages)
# print('physics' in languages)

#set
# days=set(["sunday","monday","tuesday","wednesday","thursday","friday","sarturday"])
# print(days)
# print(type(days))
# for i in days:
#     print(i)

#adding items to a set
#using add method 
# names=set(["rarar","gfgfhfj","yrgrh","qaaerer"])
# print(names)
# names.add("ggg")
# print(names)

#using update function
# names=set(["rarar","gfgfhfj","yrgrh","qaaerer"])
# print(names)
# names.update(["ggg","ttt"])
# print(names)

#removing items from a set
#using discard method
# names=set(["rarar","gfgfhfj","yrgrh","qaaerer"])
# print(names)
# names.discard("rarar")
# print(names)

# #using remove method
# names=set(["rarar","gfgfhfj","yrgrh","qaaerer"])
# print(names)
# names.remove("gsghjqu")
# print(names)

#union 
# days1={"sun","mon","tues"}
# days2={"wed","thur","friday","sat"}
# print(days1|days2)

# days1={"sun","mon","tues"}
# days2={"wed","satur","sun","mon"}
# print(days1|days2)

#intersection
# days1={"sun","mon","tues"}
# days2={"wed","satur","sun","mon"}
# print(days1&days2)

#set comparisons
# days1={"monday","tuesday","wednesday","thursday","friday"}
# days2={"thursday","friday"}
# days3={"tuesday","wednesday","monday"}

# print(days1>days2)

# print(days2>days1)

# print(days2==days3)

#create a dictionary in python
# capital_city={"nepal":"kathmandu","italy":"rome"}
# print(capital_city)

# print(capital_city["nepal"])

#add elements to a python dictionary
# capital_city={"nepal":"kathmandu","italy":"rome"}
# print("initial dictionary: ",capital_city)
# capital_city["japan"]="tokyo"
# print("update dictionary: ",capital_city) 

#change value of dictionary
# student_id={1:"jennifer",2:"jackson",3:"kardhasian"}
# print("initial dictionary: ",student_id)
# student_id[2]="clara"
# print("updated dictionary: ",student_id)

#accessing elements from a dictionary
# student_id={1:"jennifer",2:"jackson",3:"kardhasian"}
# print(student_id[1])
# print(student_id[3])
# print(student_id[2])

#delete elements from a dictionary
# student_id={1:"jennifer",2:"jackson",3:"kardhasian"}
# print("initial dicrionary: ",student_id)
# del student_id[3]
# print("updated dictionary: ",student_id)

#iterating through a dictionary
# squares={1:1,2:4,3:9,4:16,5:25}
# for i in squares:
#     print(squares[i])

#string interpolation
# print(f"{a} and {b}")

#if statement
# i=13
# if(i<20):
#     print("13 is less than 20")
# print("im NOT in if")

#if else statement
# i=30
# if(30<20):
#     print("is greater than 20")
# else:
#     print("30 is smaller than 20")

#nested if statement    
# i=10
# if(i==10):
#     if(i<15):
#         print("i is smaller than 15")
#     if(i<12):
#       print("i is smaller than 12 too")
#     else:
#       print("i is greater then 15")    

#if elif else ladder
# i=30
# if(i==20):
#     print("i is 20")
# elif(i==35):
#     print("i is 35")
# elif(i==30):
#     print("i is 30")
# else:
#     print("i is not present")            

#odd or even
# a=int(input("enter your number"))
# if(a%2==0):
#     print("a is even")
# else:
#     print("a is odd")

#+ve and -ve number
# a=int(input("enter your number"))
# if(a>0):
#     print("a is a positive integer")
# elif(a==0):
#     print("a is zero")  
# else:
#     print("a is a negative integer")      

#vowel or not
# ch=(input("enter the ch"))
# if(ch=="a"):
#     print("ch is a vowel")
# elif(ch=='e'):
#      print("ch is a vowel")
# elif(ch=='i'):
#      print("ch is a vowel")     
# elif(ch=='o'):
#      print("ch is a vowel")  
# elif(ch=='u'):
#      print("ch is a vowel")  
# else:
#     print("ch is not a vowel")    

#grading system
# score=int(input("enter the score"))
# if(score<=100 and score>-1):
#     if(score<=100 and score>=90):
#         print("A+")
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
               

#calculator

# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# option=int(input("Enter your option"))
# if option==1:
#     a=int(input("enter your number a :"))
#     b=int(input("enter your number b:"))
#     sum=a+b
#     print(sum)
# if option==2:
#     a=int(input("enter your number a :"))
#     b=int(input("enter your number b:"))
#     sum=a-b
#     print(sum) 
# if option==3:
#     a=int(input("enter your number a :"))
#     b=int(input("enter your number b:"))
#     sum=a*b
#     print(sum) 
# if option==4:
#     a=int(input("enter your number a :"))
#     b=int(input("enter your number b:"))

#     if(b==0):
#         print("invalid condition") 
#     else:
#         sum=(a/b)
#         print(sum)

#leap year
# year=int(input("Enter the year:"))
# if(year%4==0):
#     print("its a leap year")
# else:
#     print("not a leap year")  

#greatest of 3 numbers
# a=int(input("Enter the first number: ")) 
# b=int(input("Enter the second number: ")) 
# c=int(input("Enter the third number: "))
# if(a>b) and (a>c):
#     print("a is the greatest")
# elif(b>a) and (b>c):
#     print("b is the greatest number")
# else:
#     print("c is the greatest number")       


