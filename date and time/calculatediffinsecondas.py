
from datetime import datetime

# Input format: DD-MM-YYYY HH:MM:SS
fmt = "%d-%m-%Y %H:%M:%S"

# Sample Inputs
timestamp1 = "01-01-2023 10:00:00"
timestamp2 = "01-01-2023 10:01:30"

# Parse strings into datetime objects
t1 = datetime.strptime(timestamp1, fmt)
t2 = datetime.strptime(timestamp2, fmt)

# Calculate absolute difference in seconds
difference = int(abs((t2 - t1).total_seconds()))

print(difference) # Output: 90
