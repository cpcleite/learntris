m = [['.' for i in range(10)] for j in range(22)]
score = 0
cleared_lines = 0
tetramino = []
b = False
shift_h = 0
shift_v = 0

while True:
    if b:
        break

    aux = []
    escape = False
    for l in input():
        match l:
            case '?':
                escape = True
            case ' ':
                pass
            case _:
                if escape:
                    aux.append('?' + l)
                else:
                    aux.append(l)

    for com in aux:
        match com:
            case 'q':
                b = True

            case 'p':
                for l in m:
                    print(' '.join(l))

            case 'g':
                for i in range(22):
                    l = input()
                    m[i] = [x for x in l if x != ' ']

            case 'c':
                m = [['.' for i in range(10)] for j in range(22)]

            case '?s':
                print(score)

            case '?n':
                print(cleared_lines)

            case 's':
                for i, l in enumerate(m):
                    if not ('.' in l):
                        score += 100
                        cleared_lines += 1
                        m[i] = 10 * ['.']

            case 'I':
                tetramino = [4 * ['.'], 4 * ['c'],  4 * ['.'],  4 * ['.']]

            case 'O':
                tetramino = 2 * [2 * ['y']]

            case 'Z':
                tetramino = [['r', 'r', '.'], ['.', 'r', 'r'], ['.', '.', '.']]

            case 'S':
                tetramino = [['.', 'g', 'g'], ['g', 'g', '.'], ['.', '.', '.']]

            case 'J':
                tetramino = [['b', '.', '.'], ['b', 'b', 'b'], ['.', '.', '.']]

            case 'L':
                tetramino = [['.', '.', 'o'], ['o', 'o', 'o'], ['.', '.', '.']]

            case 'T':
                tetramino = [['.', 'm', '.'], ['m', 'm', 'm'], ['.', '.', '.']]

            case ')':
                tetramino = [[tetramino[l][c] for l in range(
                    len(tetramino)-1, -1, -1)] for c in range(len(tetramino[0]))]

            case '(':
                tetramino = [[tetramino[l][c] for l in range(
                    len(tetramino))] for c in range(len(tetramino[0]))]

            case ';':
                print()

            case 't':
                for l in tetramino:
                    print(' '.join(l))

            case 'P':

                # calculates Tetramino's width
                width = len(tetramino[0])

                for l in range(len(tetramino)-1, -1, -1):
                    if sum([tetramino[x][l] != '.'
                            for x in range(len(tetramino))]):
                        break
                    else:
                        width -= 1

                # calculates Tetramino's height
                height = len(tetramino)

                for l in range(len(tetramino)-1, -1, -1):
                    if sum([x != '.' for x in tetramino[l]]):
                        break
                    else:
                        height -= 1

                fill = (len(m[0]) - len(tetramino[0])) // 2 + shift_h

                fill = min(len(m[0]) - width, fill)

                shift_v = min(len(m) - height, shift_v)

                for l in range(shift_v):
                    print(' '.join(len(m[0]) * '.'))

                for l in tetramino[:height]:
                    aux = [x.upper() for x in l]
                    aux = fill * ['.'] + aux + len(m[0]) * ['.']
                    aux = aux[: len(m[0])]
                    print(' '.join(aux))

                for l in m[:-height - shift_v]:
                    print(' '.join(l))

            case '<':
                shift_h -= 1

            case '>':
                shift_h += 1

            case 'v':
                shift_v += 1
