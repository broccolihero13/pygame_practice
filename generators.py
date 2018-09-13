import random

def number_generator(my_str, i):
    for i in range(random.randint(1, i)):
        yield (my_str,i)

startNum = number_generator("First", 15)

print(list(startNum))

# generator expression
name_list = ['Brock', 'Monique', 'Brian', 'Francesqua', 'Alexis', 'Shirley']

print(list(name.upper() for name in name_list))

# generator object
def odd_number_generator(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

odd_ints = odd_number_generator(20)
odd_ints.__next__()
odd_ints.__next__()
print(odd_ints.__next__())
