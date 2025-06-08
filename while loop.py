#print numbers from 1 to 10 using while loop
# number = 10
# while number >= 1:
#     print(number)
#     number -= 1 

# #sum of digits using while loop
# a = int(input("Enter the number: "))
# b = 0  
# while a > 0:
#     b += a%10
#     a=a//10 
# print(b)

# a = int(input("Enter the number: "))
# b=0  
# while a!=-1:
#     b+=a
#     a = int(input("Enter the number: "))
# print(b)    

#nested loop
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()


# a=1
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print(a,end=" ")
#         a += 1
#     print()    


# n=6
# for i in range(0,n):
#     for j in range(0,i):
#         print("* ",end=" ")
#     print()    


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="  ")
#     for k in range(i):
#         print("* ",end=" ")    
#     print() 


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("",end="  ")
#     for k in range(i):
#         print("*  ",end=" ")    
#     print()     


# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print("* ",end=" ")
#     print()  


# n=6
# for i in range(1,n+1):
#     for j in range(i):
#         print(" ",end="  ")
#     for k in range(n-i):    
#         print("* ",end=" ")
#     print() 

        
# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print("  ",end="")
#     for k in range(i):
#         print("*   ",end="")    
#     print()  


# n=5
# for i in range(0,n):
#     for j in range(i):
#         print("",end="   ")
#     for k in range(0,n):
#         print("* ",end="")      
#     print()


# n=5
# for i in range(0,n):
#     for j in range(n-i):
#         print("",end="  ")
#     for k in range(i):
#         print("*  ",end=" ")    
#     print()     
# for i in range(0,n):
#     for j in range(0,i):
#         print("  ",end="")
#     for k in range(n-i):
#         print("*   ",end="")    
#     print()  


# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n-i):
#         print("* ",end="")
#     print()
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("* ",end="")
#     print()                    


# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()            

 
# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print("  ",end="")
#     for k in range(2*i-1):
#         if k==0 or k==2 * i-2 or i==n:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
       

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end="")
#     for k in range(2*i-1):
#         if k==0 or k==2 * i-2 or i==n:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end="")
#     for k in range(2*i-1):
#         if k==0 or k==2 * i-2 :
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print("  ",end="")
#     for k in range(2*i-1):
#         if k==0 or k==2 * i-2:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


# a=1
# n=4
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a+=1
#     print()    


