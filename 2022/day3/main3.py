with open('text.txt') as f:
    lines = f.readlines()

elem_list = list()
first_list = list()
second_list = list()
suma = 0

for line in lines:
    single_line = line.strip()
    line_splitted = list(single_line)
    # print(line_splitted)
    # print(len(line_splitted))
    counter = 1
    for elem in line_splitted:
        if counter <= len(line_splitted) / 2:
            first_list.append(elem)
            counter += 1
        else:
            second_list.append(elem)
            counter += 1
    # print(first_list)
    # print(second_list)
    common = list(set(first_list).intersection(second_list))
    print(common)
    if common[0] == "a":
        suma += 1
    if common[0] == "b":
        suma += 2
    if common[0] == "c":
        suma += 3
    if common[0] == "d":
        suma += 4
    if common[0] == "e":
        suma += 5
    if common[0] == "f":
        suma += 6
    if common[0] == "g":
        suma += 7
    if common[0] == "h":
        suma += 8
    if common[0] == "i":
        suma += 9
    if common[0] == "j":
        suma += 10
    if common[0] == "k":
        suma += 11
    if common[0] == "l":
        suma += 12
    if common[0] == "m":
        suma += 13
    if common[0] == "n":
        suma += 14
    if common[0] == "o":
        suma += 15
    if common[0] == "p":
        suma += 16
    if common[0] == "q":
        suma += 17
    if common[0] == "r":
        suma += 18
    if common[0] == "s":
        suma += 19
    if common[0] == "t":
        suma += 20
    if common[0] == "u":
        suma += 21
    if common[0] == "v":
        suma += 22
    if common[0] == "w":
        suma += 23
    if common[0] == "x":
        suma += 24
    if common[0] == "y":
        suma += 25
    if common[0] == "z":
        suma += 26
    if common[0] == "A":
        suma += 27
    if common[0] == "B":
        suma += 28
    if common[0] == "C":
        suma += 29
    if common[0] == "D":
        suma += 30
    if common[0] == "E":
        suma += 31
    if common[0] == "F":
        suma += 32
    if common[0] == "G":
        suma += 33
    if common[0] == "H":
        suma += 34
    if common[0] == "I":
        suma += 35
    if common[0] == "J":
        suma += 36
    if common[0] == "K":
        suma += 37
    if common[0] == "L":
        suma += 38
    if common[0] == "M":
        suma += 39
    if common[0] == "N":
        suma += 40
    if common[0] == "O":
        suma += 41
    if common[0] == "P":
        suma += 42
    if common[0] == "Q":
        suma += 43
    if common[0] == "R":
        suma += 44
    if common[0] == "S":
        suma += 45
    if common[0] == "T":
        suma += 46
    if common[0] == "U":
        suma += 47
    if common[0] == "V":
        suma += 48
    if common[0] == "W":
        suma += 49
    if common[0] == "X":
        suma += 50
    if common[0] == "Y":
        suma += 51
    if common[0] == "Z":
        suma += 52
    print(suma)
    first_list.clear()
    second_list.clear()
print(suma)
