n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
def calAverage(query_name):
    temp = 0
    for mark in student_marks[query_name]:
        temp += mark
    average = temp / len(query_name[scores])
    return average
calAverage(query_name)