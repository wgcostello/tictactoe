winning_combos = [[(0, 0), (0, 1), (0, 2)],
                  [(1, 0), (1, 1), (1, 2)],
                  [(2, 0), (2, 1), (2, 2)],
                  [(0, 0), (1, 0), (2, 0)],
                  [(0, 1), (1, 1), (2, 1)],
                  [(0, 2), (1, 2), (2, 2)],
                  [(0, 0), (1, 1), (2, 2)],
                  [(2, 0), (1, 1), (0, 2)]]


def victory(locations):
    for c in winning_combos:
        if all(c[i] in locations for i in range(3)):
            return True
    else:
        return False


# Print empty field
print('-' * 9)
for i in range(3):
    print('|' + ' ' * 7 + '|')
print('-' * 9)

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3 * i, 3 * (i + 1)):
        matrix[i].append(' ')

X_locations = []
O_locations = []
empty_locations = [(i, j) for i in range(3) for j in range(3)]

finished = False
turn = 1

while not finished:
    accepted = False

    while not accepted:
        coordinates = input("Enter the coordinates: ")
        coordinates = coordinates.split()
        if any([ord(c) < 48 or ord(c) > 58 for j in (0, 1) for c in coordinates[j]]):
            print("You should enter numbers!")
            continue
        else:
            x = int(coordinates[0])
            y = int(coordinates[1])
            if x not in range(1, 4) or y not in range(1, 4):
                print("Coordinates should be from 1 to 3!")
                continue
            else:
                if (3 - y, x - 1) not in empty_locations:
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    accepted = True
    else:
        if turn % 2 != 0:
            matrix[3 - y][x - 1] = 'X'
            X_locations.append((3 - y, x - 1))
            empty_locations.remove((3 - y, x - 1))
        else:
            matrix[3 - y][x - 1] = 'O'
            O_locations.append((3 - y, x - 1))
            empty_locations.remove((3 - y, x - 1))

        print('-' * 9)
        for i in range(3):
            print('| ' + ' '.join(matrix[i]) + ' |')
        print('-' * 9)

    X_wins = victory(X_locations)
    O_wins = victory(O_locations)

    # Impossible
    if (X_wins and O_wins) or abs(len(X_locations) - len(O_locations)) >= 2:
        print('Impossible')
    # Draw
    elif not X_wins and not O_wins and len(empty_locations) == 0:
        print('Draw')
        finished = True
    # X wins
    elif X_wins and not O_wins:
        print('X wins')
        finished = True
    # O wins
    elif O_wins and not X_wins:
        print('O wins')
        finished = True
    # Game not finished
    elif not X_wins and not O_wins and len(empty_locations) > 0:
        turn += 1
