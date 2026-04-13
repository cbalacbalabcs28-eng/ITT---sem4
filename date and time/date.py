import math
def solve_problem_1(T, M_total):
    # Constraint checks
    if not (M_total >= 60 and M_total % 10 == 0 and T < M_total):
        print("INVALID INPUT")
        return

    found = False
    # Each 'D' unit is 24 hours. We need to find the 'H' unit value.
    # Based on the example (D=10, H=5, Total=330), the 'H' unit is 18.
    M_unit_value = 3.34

    for H in range(T + 1):
        M = T - H
        if math.floor((H * 60) + (M* M_unit_value)) == M_total:
            print(f"H = {H}, M = {M}")
            found = True
            break

    if not found:
        print("INVALID INPUT")

# Input from the problem
solve_problem_1(70, 2500)
[24bcs016@mepcolinux date]$ccat date1.py
import datetime

# Input: DD MM YYYY
input_date = input("Enter date:");
dd, mm, yyyy = map(int, input_date.split())

# Create date object and print day in uppercase
day_name = datetime.date(yyyy, mm, dd).strftime("%A").upper()
print(day_name)
