import timeit
setup_code = """
import math
"""
main_code = """
for i in range(1000000):
	foo = math.sqrt(i)
"""
print(timeit.timeit(stmt=main_code,
setup=setup_code,
number=100))