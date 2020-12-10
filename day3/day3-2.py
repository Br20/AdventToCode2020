file = open("day3.txt")
content = file.read()
input = content.split("\n")
input.pop(len(input)-1)
row = 0
column = 0
trees = 0
slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]
totalMul = 1
for i in range(len(slopes)):
    row = 0
    column = 0
    trees = 0
    while ( row <= len(input)-1):
        if (column > len(input[0])-1):
            column = column - len(input[0])
        if (input[row][column] == "#"):
            trees+=1
        row+=slopes[i][0]
        column+=slopes[i][1]
    totalMul *= trees
print(totalMul)

#Out: 6050183040
