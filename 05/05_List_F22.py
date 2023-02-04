def upgrade(grades, upgrade_list):

    grade_mapper = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A']

    for student in grades:
        if student[0] in upgrade_list:
            _, grade = student
            i = grades.index(student)
            a = grade_mapper.index(grade)
            grades[i][1] = grade_mapper[a+1]

    grades.sort()
    
def index_of(grades, uid):
    i = -1
    for index, student in enumerate(grades):
        if student[0] == uid:
            i = index      
    return i

exec(input()) 
exec(input())  
exec(input())