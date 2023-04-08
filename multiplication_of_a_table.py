# #wap to print multiplication table of a given number

#using while loop

n = int(input("Enter the number: "))
i=1
while(i<=10):
    print(n,"X",i,"=",n*i)
    i=i+1

#Using for loop
# n = int(input("Enter the number : "))
# for i in range(1,11):
#     print(n*i)

#multiplication table from 2 to 20
# n = int(input("Enter Number less than 20: "))
# print("Multiplication table: ")
#
# for i in range(n,10):
#     for j in range(1,11):
# print('{0}*{1}={2}'.format(i,j,i*J))
#     print('')