P = int(input("Enter Principal amount:"));
R = int(input("Enter Rate of interest:"));
T = int(input("Enter Time period:"));
if (P>=1 and P<=100000) or (R>=1 and R<=20) or (T>=1 and T<=10) :
   SI = (P*R*T)/100;
   print("The Simple Interest:",SI);
else:
   print("Invalid values");
