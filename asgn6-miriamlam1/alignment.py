# Assignment 6
# Sequence Alignment - greatest common subsequence
# Input: two strings and its scoring matrix
# Output: the highest scoring alignment and its score

import sys

class Alignment:
    def __init__(self, string1, string2, matrix):
        self.string1 = string1
        self.string2 = string2
        self.matrix = dict()

def populate_table(a):
    table = [[0 for x in range(len(a.string1))] for y in range(len(a.string2))]

    # base cases
    for row in range(1, len(a.string2)):
        table[row][0] = table[row-1][0] + a.matrix["-"][a.string2[row]]

    for col in range(1, len(a.string1)):
        table[0][col] = table[0][col-1] + a.matrix[a.string1[col]]["-"]

    # populating table
    for row in range(1,len(a.string2)):
        for col in range(1,len(a.string1)):

            score = a.matrix[a.string1[col]][a.string2[row]]

            up = table[row-1][col] + a.matrix["-"][a.string2[row]]
            diag = table[row-1][col-1] + score
            left = table[row][col-1] + a.matrix[a.string1[col]]["-"]

            table[row][col] = max(left, diag, up)

    # print(a.string1)
    # for i in range(len(table)):
    #     print(a.string2[i] , table[i])
    # print("")

    backtrack(a,table)

def backtrack(a, table):
    col = len(a.string1)-1
    row = len(a.string2)-1
    #print(a.string1)
    #print(a.string2)
    x = ""
    y = ""
    while(1):
        if row <= 0 and col <= 0:
            break
        else:
            score = a.matrix[a.string1[col]][a.string2[row]]
            up = table[row-1][col] + a.matrix["-"][a.string2[row]]
            diag = table[row-1][col-1] + score
            left = table[row][col-1] + a.matrix[a.string1[col]]["-"]
            if diag == table[row][col]:
                y = a.string1[col] +" "+ y
                x = a.string2[row] +" "+ x
                row -=1
                col -=1
                #print("diag")
            elif up == table[row][col]:
                y = "- " + y
                x = a.string2[row]+" " + x
                row -=1
                #print("up")
            elif left == table[row][col]:
                x = "- " + x
                y = a.string1[col] +" " + y
                col -=1
                #print("left")

    print("x:", y)
    print("y:", x)
    print("Score:", table[len(a.string2)-1][len(a.string1)-1])


def get_file(file):
    f = open(file, "r")
    file_list = []
    for line in f:
        file_list.append(line)  
    f.close()

    a = Alignment("","",dict())

    a.string1 = "-" + file_list[0].strip()
    a.string2 = "-" + file_list[1].strip()

    for i in range(3,len(file_list)):
        line = file_list[i].split()
        b = dict()
        for i in range(1,len(line)):
            b[file_list[i+2][0]] = int(line[i])
        a.matrix[line[0]] = b

    return a

def main():
    a = get_file(sys.argv[1])
    populate_table(a)


if __name__ == "__main__":
    main()

