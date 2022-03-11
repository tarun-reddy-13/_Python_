num=int(input("Enter any integer : "))
i=1;sum=0
for i in range(1,21):
    if i%2==0:
        print(i," ")
        sum=sum+i
print("Sum of even series from 1 to",num,"is :",sum)