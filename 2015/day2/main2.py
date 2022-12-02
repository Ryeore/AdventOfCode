with open('text.txt', 'r') as file:
    lines = file.readlines()

# print(lines)

lista = list()
smallest = list()
total = 0
total_ribbon = 0
short = list()
for line in lines:
    lista.append(line.strip())

# print(lista)

for elem in lista:
    wymiar = elem.split("x")
    L = int(wymiar[0])
    short.append(L)
    W = int(wymiar[1])
    short.append(W)
    H = int(wymiar[2])
    short.append(H)
    short.remove(max(short))
    ribbon = 2*short[0]+2*short[1]+L*W*H
    # print(ribbon)
    surf1 = L*W
    smallest.append(surf1)
    surf2 = W*H
    smallest.append(surf2)
    surf3 = H*L
    smallest.append(surf3)
    pick_smallest = min(smallest)
    surface = 2*surf1 + 2*surf2 + 2*surf3 + pick_smallest
    # print(surface)
    total_ribbon += ribbon
    total += surface
    smallest.clear()
    short.clear()

print(total)
print(total_ribbon)


''' 
l w h   | 2*l*w + 2*w*h + 2*h*l
'''
