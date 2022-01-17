m = [['.' for i in range(10)] for j in range(22)]
score = 0
cleared_lines = 0
b = False
start_screen = False
paused = False
game_over = False


class Tetramino():
    def __init__(self, kind=None):
        self.shift_h = 0
        self.shift_v = 0

        match kind:
            case None:
                self.cells = []
                self.height = 0
                self.width = 0

            case 'I':
                self.cells = [4 * ['.'], 4 * ['c'],  4 * ['.'],  4 * ['.']]
                self.height = 4
                self.width = 2

            case 'O':
                self.cells = 2 * [2 * ['y']]
                self.height = 2
                self.width = 2

            case 'Z':
                self.cells = [['r', 'r', '.'],
                              ['.', 'r', 'r'],
                              ['.', '.', '.']]
                self.height = 2
                self.width = 3

            case 'S':
                self.cells = [['.', 'g', 'g'],
                              ['g', 'g', '.'],
                              ['.', '.', '.']]
                self.height = 2
                self.width = 3

            case 'J':
                self.cells = [['b', '.', '.'],
                              ['b', 'b', 'b'],
                              ['.', '.', '.']]
                self.height = 2
                self.width = 3

            case 'L':
                self.cells = [['.', '.', 'o'],
                              ['o', 'o', 'o'],
                              ['.', '.', '.']]
                self.height = 2
                self.width = 3

            case 'T':
                self.cells = [['.', 'm', '.'],
                              ['m', 'm', 'm'],
                              ['.', '.', '.']]
                self.height = 2
                self.width = 3

        self._set_fill()

    def _set_fill(self):

        if len(self.cells) == 0:
            self.fill = len(m[0]) // 2
            self.shift_h = 0
        else:
            # Calculates left filler
            self.fill = (len(m[0]) - len(self.cells[0])
                         ) // 2 + self.shift_h
            self.fill = max(self.fill, 0)
            self.fill = min(self.fill, len(m[0]) - self.width)
            self.shift_h = self.fill - \
                (len(m[0]) - len(self.cells[0])) // 2

    def _get_width(self):
        # calculates Tetramino's width
        width = len(self.cells[0])

        for l in range(len(self.cells)-1, -1, -1):
            if sum([self.cells[x][l] != '.'
                    for x in range(len(self.cells))]):
                break
            else:
                width -= 1

        return width

    def _get_height(self):
        # calculates Tetramino's height
        height = len(self.cells)

        for l in range(len(self.cells)-1, -1, -1):
            if sum([x != '.' for x in self.cells[l]]):
                break
            else:
                height -= 1

        return height

    def rot_clock(self):
        self.cells = [[self.cells[l][c] for l in range(
            len(self.cells)-1, -1, -1)] for c in range(len(self.cells[0]))]

        self.width = self._get_width()
        self.height = self._get_height()

    def rot_cclock(self):
        self.cells = [[self.cells[l][c] for l in range(
            len(self.cells))] for c in range(len(self.cells[0]))]

        self.width = self._get_width()
        self.height = self._get_height()

    def __repr__(self) -> str:
        return '\n'.join([' '.join(l) for l in tetramino.cells])

    def detect_collision(self):

        for l in range(self.height-1, -1, -1):
            for c in range(len(self.cells[0])-1, -1, -1):
                if self.cells[l][c] != '.' and \
                        m[self.shift_v + l][self.fill + c] != '.':
                    return True

        return False


tetramino = Tetramino()


def new_matrix(upper=False):
    global tetramino

    if len(tetramino.cells) == 0:
        return m.copy()

    # Appends top filler
    new_m = m[:tetramino.shift_v]

    # Appends tetramino
    for i, l in enumerate(tetramino.cells[:tetramino.height]):
        if upper:
            aux = [x.upper() for x in l]
        else:
            aux = l

        for j in range(tetramino.width):
            if m[tetramino.shift_v + i][tetramino.fill + j] != '.':
                aux[j] = m[tetramino.shift_v + i][tetramino.fill + j]

        aux = m[tetramino.shift_v + i][:tetramino.fill] + \
            aux + len(m[0]) * ['.']
        aux = aux[: len(m[0])]

        new_m.append(aux)

    # Appends bottom
    new_m.extend(m[tetramino.height + tetramino.shift_v:])

    return new_m


while True:
    if b:
        break

    # Parse Input commands
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

    # Process Commands
    for com in aux:
        match com:
            case 'q':  # quit
                b = True

            case 'p':  # print matrix + tetramino
                if start_screen:
                    print('Learntris (c) 1992 Tetraminex, Inc.')
                    print('Press start button to begin.')

                elif paused:
                    print('Paused')
                    print('Press start button to continue.')

                else:
                    nm = new_matrix(upper=False)
                    for l in nm:
                        print(' '.join(l))

            case 'g':  # input matrix
                for i in range(22):
                    l = input()
                    m[i] = [x for x in l if x != ' ']

            case 'c':  # clear matrix
                m = [['.' for i in range(10)] for j in range(22)]

            case '?s':  # print score
                print(score)

            case '?n':  # print cleared lines
                print(cleared_lines)

            case 's':
                for i, l in enumerate(m):
                    if not ('.' in l):
                        score += 100
                        cleared_lines += 1
                        m[i] = 10 * ['.']

            case 'I' | 'O' | 'Z' | 'S' | 'J' | 'L' | 'T':
                tetramino = Tetramino(com)

            case ')':
                tetramino.rot_clock()

            case '(':
                tetramino.rot_cclock()

            case ';':
                print()

            case 't':
                print(tetramino)

            case 'P':
                nm = new_matrix(upper=True)
                for l in nm:
                    print(' '.join(l))

                if game_over:
                    print('Game Over')

            case '<':
                tetramino.shift_h -= 1
                tetramino._set_fill()

                if tetramino.detect_collision():
                    tetramino.shift_h += 1
                    tetramino._set_fill()

            case '>':
                tetramino.shift_h += 1
                tetramino._set_fill()

                if tetramino.detect_collision():
                    tetramino.shift_h -= 1
                    tetramino._set_fill()

            case 'v':
                tetramino.shift_v += 1
                tetramino.shift_v = min(len(m) - tetramino.height,
                                        tetramino.shift_v)

                if tetramino.detect_collision():
                    tetramino.shift_v -= 1

            case 'V':
                for l in range(tetramino.shift_v, len(m) - tetramino.height):
                    tetramino.shift_v += 1
                    if tetramino.detect_collision():
                        tetramino.shift_v -= 1
                        break

                m = new_matrix(upper=False)

                if sum([x != '.' for x in m[0]]) > 0:
                    game_over = True

            case '@':
                start_screen = True

            case '!':
                if start_screen:
                    m = [['.' for i in range(10)] for j in range(22)]
                    score = 0
                    cleared_lines = 0
                    tetramino = Tetramino()
                    start_screen = False

                elif paused:
                    paused = False

                else:
                    paused = True
