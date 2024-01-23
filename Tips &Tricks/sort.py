data = [ 10, 3, 1, 4, 5]
sorted_data = sorted(data)
print(sorted_data)

data = [ {"name" : "loki", 'age' : 19},
         {"name": "raju", 'age': 17},
         {"name": "ram", 'age': 21}]
sorted_data = sorted(data, key= lambda x : x["age"])
print(sorted_data)
