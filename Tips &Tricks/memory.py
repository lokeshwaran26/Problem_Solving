import sys

my_list = [ i for i in range(1000)]
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(1000))
print(sys.getsizeof(my_gen), "bytes")
