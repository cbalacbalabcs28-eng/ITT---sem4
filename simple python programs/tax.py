salary = float(input("Enter your salary(in LPA):"));
if salary<=2.5:
   tax=0;
   print("No tax");
elif salary>2.5 and salary<=5:
   tax = (salary-2.5)*0.05;
   print("there will be 5% of tax",tax);
elif salary>5 and salary<=10:
   tax = 0.125+(salary-5.0)*0.10;
   print("There will be 10% of tax",tax);
elif salary>10:
   tax = 0.125+0.5+(salary - 10.0 )*0.15;
   print("There will be 15% of tax",tax);
else:
   print("valid salary");
