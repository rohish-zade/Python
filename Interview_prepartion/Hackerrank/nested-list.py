# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    # Create an empty list to store student data.
    students = []

    for _ in range(int(input())):
        name = input()  # Student name
        score = float(input())  # Student grade (score)
        students.append([name, score])  # Add [name, score] pair to the students list
    
    # Extracting all the scores to find unique grades
    scores = sorted({student[1] for student in students})
    
    # Find the second lowest score
    second_lowest_score = scores[1]
    
    # List comprehension to find names of students with the second lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Output each name on a new line
    for name in second_lowest_students:
        print(name)

