a=0;b=1;sum=0;i=1
num=int(input("Enter any number : "))
print("Fibonacci series : ",a,b,end=" ")
for i in range(3,num):
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum
