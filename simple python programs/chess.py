t_cases = int(input())

for _ in range(t_cases):

    x = int(input())

    results = input().strip()

    chandru_pts = 0
    nirmal_pts = 0


    for move in results:
        if move == 'C':
            chandru_pts += 2
        elif move == 'N':
            nirmal_pts += 2
        elif move == 'D':
            chandru_pts += 1
            nirmal_pts += 1


    if chandru_pts > nirmal_pts:

        print(60 * x)
    elif nirmal_pts > chandru_pts:

        print(40 * x)
    else:

        print(55 * x)
