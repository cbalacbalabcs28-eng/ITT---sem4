try:
    data = input().split()

    # 2. Convert to integers (catches non-integers)
    a = int(data[0])
    b = int(data[1])

    # 3. Perform division (catches division by zero)
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Division by zero")

except ValueError:
    print("Error: Invalid input")

except IndexError:
    print("Error: Please provide two values")
