import random

string = ''
for i in range(1000000):
    string += '%c' %random.randint(97, 122)

with open('string.txt', 'w') as f:
        f.write(string)

print('[DONE!]')