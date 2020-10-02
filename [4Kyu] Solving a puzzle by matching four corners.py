# https://www.codewars.com/kata/5ef2bc554a7606002a366006

def puzzle_solver(pieces, width, height):
    g_line = {}
    inne = {}
    wynik = [[[""] for _ in range(width)] for _ in range(height)]
    for x in pieces:
        if x[0].count(None) == 2:
            g_line[str(x[0][0])+"_"+str(x[1][0])] = (str(x[0][1])+"_"+str(x[1][1]), x[2], str(x[1][0])+"_"+str(x[1][1]))
        else:
            inne[str(x[0][0])+"_"+str(x[0][1])] = (str(x[1][0])+"_"+str(x[1][1]), x[2])
    wynik[0][0] = g_line["None_None"][1:3]
    x = 1
    next = g_line["None_None"][0]
    while x != width:
        wynik[0][x] = g_line[next][1:3]
        next = g_line[next][0]
        x += 1
    for y in range(width):
        next = wynik[0][y][1]
        wynik[0][y] = wynik[0][y][0]
        for x in range(1, height):
            wynik[x][y] = inne[next][1]
            next = inne[next][0]

    return [tuple(x) for x in wynik]
