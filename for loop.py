#the for loop
# numbers=[1,2,3,4,5,6,7]
# square=0
# squares=[]
# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("The list of squares is",squares)    

#using else statement with for loop
# string="I love apples"
# for s in string:
#     if s=="p":
#         print("if block")
# else:
#     print(s)        

#the range() function
# print(range(15))    
# print(list(range(15)))
# print(list(range(4,9)))
# print(list(range(5,25,4)))

# tuple_=("python","loops","iteration","condition","range")
# for iterator in range(len(tuple_)):
#     print(tuple_[iterator].upper())

#sum of natural numbers
# a=int(input("Enter the number"))
# b=0
# for i in range(0,a+1):
#     b += i
# print(b)    
    
# a=int(input("Enter the number"))
# b=int(input("Enter the range"))
# for i in range(1,b+1):
#     print(i,"x",a,"=",i*a)

 #factorial
# a=int(input("enter the number"))
# b=1
# for i in range(1,a+1):
#     b *= i   
# print(b)

#Fibanocci series
# a, b = 0, 1
# n = int(input("Enter the number of terms: "))
# print("Fibonacci Series:")
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

#find sum of all even numbers from 1 to n
# n=int(input("Enter the number"))
# a=0
# for i in range(0,n+1,2):
#     a += i
# print(a)


#count vowels in a string
# string=str(input("Enter the string: "))
# vowels='aeiouAEIOU'
# count=0
# for i in string:
#     if i in vowels:
#         count += 1
# print(count)   


#find maximum number in a list
# a=[2,4,6,8,10]
# b=a[0]
# for i in a:
#     if i>b:
#         b=i
# print(b)        
 
#calculate products of all numbers
# numbers=(1,2,3)
# product = 1
# for i in numbers:
#     product *= i
# print(product)

#reverse of a string
# str=(input("Enter the string"))
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)    

#maximum number in a list
# a=[1,2,3,4,5]
# b=a[0]
# for i in a:
#     print(i)
#     if i>b:
#         b=i
# print(b)

#characters at even indicies
# string=(input("enter the string"))
# a=len(string)
# for i in range(0,a,2):
#     print(string[i])

#common elemnts from two diff lists
# a=[1,2,3,4,5,6]
# b=[2,4,6,8,10]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

#sum of all numbers
# a=int(input("enter your number :"))
# b=len(str(a))
# sum=0
# for i in range(0,b):
#     c=a%10
#     sum=sum+c
#     a//=10
# print(sum)    



   


