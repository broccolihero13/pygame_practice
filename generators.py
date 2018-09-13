import random

def NumberGenerator(my_str, i):
    for i in range(random.randint(1, i)):
        yield (my_str,i)

startNum = NumberGenerator("First", 15)

for i in range(5):
    startNum.__next__()

print("Bigger than 5")