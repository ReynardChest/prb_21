import timeit

code_to_test = """

"""

code_to_test2 = """

"""

elapsed_time1 = timeit.timeit(code_to_test, number=100)/100
elapsed_time2 = timeit.timeit(code_to_test2, number=100)/100

print('Время выполнения a =', elapsed_time1)
print('Время выполнения b =', elapsed_time2)
print('B быстрее a на =', round((1-elapsed_time2/elapsed_time1)*100, 1), '%')
