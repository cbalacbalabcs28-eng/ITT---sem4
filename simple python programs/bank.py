balance = int(input("Enter your balance:"));
amount = int(input("Enter amount to withdraw:"));
if balance>0 and amount<=balance:
   balance-=amount;
   print("The withdrawal amount is:",amount);
else:
   print("You have insufficient balance in your account");
