ids = []
grades = []
res = []

grade_mapper = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

while (e := input().strip()) != 'q':
    student_id, grade = e.split(' ')
    ids.append(student_id)
    grades.append(grade)

uids = [e for e in input().strip().split(' ')]

for student in ids:
    if student in uids:
        i = ids.index(student)
        grade = grades[i]
        gid = grade_mapper.index(grade)
        grades[i] = grade_mapper[gid+1]
    
    res.append([str(student), str(grades[ids.index(student)])])

for sid, grade in sorted(res):
    print(sid, grade)