T = int(input("Enter no of test cases:"));
for i in range(T):
   A = int(input("ENter a no of coins:"));
   B = int(input("Enter coind:"));
   C = int(input("Enter a coin:"));
   D = int(input("Enter a coin:"));
   Suresh = A
   Sundar = B
   if Suresh >= Sundar:
      Sundar += C
   else:
      Suresh += C
   if Suresh >= Sundar:
      Sundar += D
   else:
      Suresh += D
   if Suresh >= Sundar:
      print("N");
   else:
      print("S");
