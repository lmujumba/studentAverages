"""
read dictionary of lis tof students
print average of selected student
2 decimal places

"""
if __name__ == '__main__': 

    #n = int(raw_input()) deprecated
    n = int(input())

    #empty list
    student_marks = {} 

    #for student in list of student
    for _ in range(n): 
        line = input().split() 
        name, scores = line[0], line[1:] 
        scores = map(float, scores) 

        student_marks[name] = scores 

    query_name = input()

    #get list
    output = list(student_marks[query_name]) 

    avg = sum(output) / len(output)

    #2 dp
    print("%0.2f" %avg)


                    