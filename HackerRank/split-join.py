def split_and_join(line):
    # write your code here
    line = line.split(" ")
    print(line)
    return '-'.join(line)

print(split_and_join('This is string'))