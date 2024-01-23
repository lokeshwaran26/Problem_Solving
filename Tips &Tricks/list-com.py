# list comprehension

square = []
for i in range(10):
    square.append(i*i)
print(square)
    
square = [i*i for i in range(10)]
print(square)
