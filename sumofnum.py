num=int(input("Enter any number : "));
i=1;sum=0;
while num!=0:
    sum=sum+num%10;
    num=int(num/10);
print("Sun of digits in given numbers is :",sum);