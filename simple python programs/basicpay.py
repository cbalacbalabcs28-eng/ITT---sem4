bs=float(input("Enter basic pay:"));
hra = 0.2;
da = 0.1;
if bs>=500 and bs<=50000:
   gs = bs+hra+da;
   print("Simple Interest:", gs);
else:
   print("Invalid");
