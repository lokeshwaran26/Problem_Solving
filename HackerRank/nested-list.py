if __name__ == '__main__':
    score_li = []
    students_li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_li.append(name)
        score_li.append(score)

    c = dict(zip(students_li, score_li))

    [print(i[0]) for i in sorted(c.items()) if i[1] == sorted(set(score_li))[1]]