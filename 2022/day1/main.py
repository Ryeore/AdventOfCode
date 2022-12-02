with open('text.txt') as f:
    lines = f.readlines()

krasnale = list()
dictionary = dict()
wyniki = list()

count = 0
for line in lines:
    krasnale.append(line.strip())
    if line.strip() == "0":
        count += 1
        res = [eval(i) for i in krasnale]
        wyniki.append(sum(res))
        krasnale.clear()
        res.clear()
    # print("{}: {}".format(count, line.strip()))

print(max(wyniki))
wyniki.sort()
# print(wyniki)
print(sum(wyniki[len(wyniki)-3:len(wyniki)]))