file = open("day3.txt")
content = file.read()
input2 = content.split("\n")
input2.pop(len(input2)-1)
row = 0
column = 0
trees = 0
while (row <= len(input2)-1):
    if (column > len(input2[0])-1):
        column = column - len(input2[0])
    if (input2[row][column] == "#"):
        trees+=1
    row+=1
    column+=3
print(trees)

#Out: 274
