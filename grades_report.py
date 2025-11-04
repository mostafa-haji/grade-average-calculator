"""
This program reads grades from a CSV file and calculates the average for each line.
"""

import csv
def read_grades_from_input():
    grades = []
    print("Enter a grades (Put q at the end)")
    while True:
        value = input(":")       
        if value == "q" or value == "Q" :
            print("OK")
            if len(grades) == 0:
                print("Grade Not Entered")
                break
            else:     
                return grades
        else:
            grades.append(int(value))

def read_grades_from_CSV(path):
    """
    Reads grades from a CSV file and returns a list of lists of floats.

    """
    grades = []
    with open(path) as f:
        for i in csv.reader(f):
            g = []
            for it in i:
                    try:
                        g.append(float(it))
                    except ValueError:
                        print("Please enter a valid number!")
            grades.append(g)
    return grades

def write_grades_to_csv(path,):
    with open("OUTPUT.csv","w",newline="") as f:
        writer = csv.writer(f)
        rows = write_grades_to_csv(path)
        for row in rows:    
            avg = sum(it for it in row)/len(row)
            writer.writerow(row + [avg])



if __name__=="__main__":
    # print(read_grade_from_input())
    print("Hello")
    path = "test.csv"
    # print(read_grade_from_CSV(path))
    write_grades_to_csv(path)

