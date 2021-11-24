import random

listx = []
for i in range(1000000):
    num = ''
    for char in range(4):
        num += '%c' %random.randint(97, 122)
    listx.append(''.join(num))

with open('strings.txt', 'w') as f:
    for element in listx:
        f.write(element + '\n')

print('[DONE!]')