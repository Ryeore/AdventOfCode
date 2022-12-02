with open('text.txt', 'r') as file:
    data = file.read().rstrip()

print(data)

counter = 0
step = 0
for elem in data:
    if elem == "(":
        counter += 1
        step += 1
    else:
        counter -= 1
        step += 1
    if counter == -1:
        print(step)
print(counter)