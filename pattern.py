row=int(input("Enter no.of rows to be printed : "));
i=0;j=0;k=1;
for i in range(1,row):
    for j in range(1,i+1):
        print(k,end=" ");
        k+=1;
    print("\n");
