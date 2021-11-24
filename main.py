import time

with open('string.txt', 'r') as reader:
    mainText = ''.join(reader.readlines())

cases = set()
with open('strings.txt', 'r') as reader:
    for i in reader:
        char = reader.readline()
        cases.add(char.strip())

start = time.time()
counter = 0
for element in cases:
    if element in mainText:
        counter += 1

elapsed = time.time() - start
print(counter)
print('in %.0f seconds' %elapsed)
