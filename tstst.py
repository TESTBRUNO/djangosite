from random import randint


a = 20
lst = []

for i in range(a):
    lst.append(randint(1, 99))
print(lst)

i = 0

for i in range(1,10,2):
    print("hi")
    
def func(a, b, c):
    for i in range(a, b):
        yield (i-1)*c

f = func(1, 10, 3)


for i in f:
    if i % 2 == 0:
        print(i, "- чётное число")
    else:
        print(i, "- нечётное число")

adsfasdfasdfasdf