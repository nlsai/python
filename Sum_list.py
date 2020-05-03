#My Version
import timeit
code_to_test = """
l=[10,1,2,3,4,5]
print(sum(l))
"""
elapsed_time = timeit.timeit(code_to_test, number=1)/100
print(elapsed_time)


#Given Solution
import timeit
code_to_test = """
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))
"""
elapsed_time = timeit.timeit(code_to_test, number=1)/100
print(elapsed_time)
