with open('string.txt') as reader:
    mainText = "".join(reader.readlines())

cases = set()
with open('strings.txt', 'r') as reader:
    content = reader.readlines()
    for line in content:
        cases.add(line.strip())

counter = 0
L, R = 0, 1
while R <= len(mainText)-1:
    if (R - L) <= 4:
        if mainText[L:R] in cases:
            cases.remove(mainText[L:R])
            counter += 1
        R += 1
    else:
        L += 1
        R = L+1

print(counter)