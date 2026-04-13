code = input("Enter a code:")
guess = input("Enter guess:")
hit = 0
nhit = 0
for i in range(len(code)):
   if code[i] == guess[i]:
      hit = hit+1
print(hit)
for i in range(len(code)):
   for j in range(len(guess)):
      if code[i] == guess[j]:
         nhit = nhit+1
print(nhit)
