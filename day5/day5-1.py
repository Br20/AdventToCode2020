import math

def nextStep(indication,row,column):
    if(indication == "F"):
        row[1] = math.floor((row[1]+row[0])/2)
    else:
        if (indication == "B"):
            row[0] = math.floor(((row[1]+row[0])/2)+1)
        else:
            if (indication == "R"):
                column[0] = math.floor(((column[1]+column[0])/2)+1)
            else:
                column[1] = math.floor((column[1]+column[0])/2)


file = open('day5.txt')
content = file.read()
boardingPasses = content.split("\n")
greatest = -1
for bp in boardingPasses:
    row = [0,127]
    column = [0,7]
    for indication in bp:
        nextStep(indication,row,column)
    op=row[0]*8 + column[0]
    if (op > greatest):
        greatest = op
print(greatest)
#Out: 822
