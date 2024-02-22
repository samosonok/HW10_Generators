# Implement a generator function (using the yield operator)
# that returns one member at a time of a numerical sequence
# whose law is defined by a user-defined function.
# In addition, the parameters of the generator function
# should be the value of the first member of the progression
# and the number of members that the sequence yields (n).
# The generator should stop its operation upon reaching the n-th member.


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
