import timeit
print(timeit.timeit('[x**2 for x in range(10)]')) #gives the average time it takes to run a specific code written inside the string
print(timeit.timeit('list(map(lambda x:x**2,range(10)))'))
