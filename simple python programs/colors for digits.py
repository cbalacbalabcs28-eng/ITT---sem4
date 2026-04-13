    0 → red
    1 → blue
    2 → green

def print_colors(sequence):
    color_map = {'0': 'red', '1': 'blue', '2': 'green'}
    result = []
    for ch in sequence:
        if ch in color_map:
            result.append(color_map[ch])
    print(' and '.join(result))

# Get input from user
seq = input("Enter the sequence of digits (0,1,2): ")

print_colors(seq)
