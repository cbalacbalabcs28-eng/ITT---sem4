n = int(input("Enter a number:"));
total=0;
if n>=1 and n<=100000:
   for i in range(1,n+1):
      total+=i;
   print(total);
