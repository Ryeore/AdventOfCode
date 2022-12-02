'''
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

'''

with open('text.txt') as f:
    lines = f.readlines()

lista = list()
punkty = 0
pozycje = {"rock": ["A", "X"], "paper": ["B", "Y"], "scissors": ["C", "Z"]}

for line in lines:
    lista = [elem for elem in line.strip() if elem]
    print(lista)
    if lista[1] == 'X':
        punkty += 0 #lose
        if lista[0] == 'A':
            punkty += 3
        if lista[0] == 'B':
            punkty += 1
        if lista[0] == 'C':
            punkty += 2
    if lista[1] == 'Y':
        punkty += 3 #draw
        if lista[0] == 'A':
            punkty += 1
        if lista[0] == 'B':
            punkty += 2
        if lista[0] == 'C':
            punkty += 3
    if lista[1] == 'Z':
        punkty += 6 #win
        if lista[0] == 'A':
            punkty += 2
        if lista[0] == 'B':
            punkty += 3
        if lista[0] == 'C':
            punkty += 1
print(punkty)
# for elem in lines:
#     lista.append(elem)
#     print(lista)
