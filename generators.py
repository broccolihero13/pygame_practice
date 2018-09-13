import random

def NumberGenerator(my_str, i):
    for i in range(random.randint(1, i)):
        yield (my_str,i)

startNum = NumberGenerator("First", 15)

print(list(startNum))

# generator expression
name_list = ['Brock', 'Monique', 'Brian', 'Francesqua', 'Alexis', 'Shirley']

print(list(name.upper() for name in name_list))