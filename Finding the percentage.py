Problem :Finding the percentage


Descp:
The user input will contain Names and marks, we have to store input in dictionary and print average marks.
Sample Input 1
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1
26.50
#############################
Code:

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores)))) 
