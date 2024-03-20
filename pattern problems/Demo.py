def find(word):
    word = string.split(' ')
    for i in word:
        for j in range(len(i)):
            if i[j] == i[j+1]:
                return i[j]

string = 'Iam hello jolly'

print(find(string))
