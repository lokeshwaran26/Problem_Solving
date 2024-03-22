if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for x in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    numer = sum(student_marks[query_name])
    deno = len(student_marks[query_name])
    avg = numer/deno
    form = "{:.2f}".format(avg)
print(form)
