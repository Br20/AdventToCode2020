import collections

file = open("day2.txt")
content = file.read()
input = content.split("\n")
input.pop(len(input)-1)
valid=0
for elem in input:
    rango = elem.split(" ")[0].split("-")
    rango[0] = int(rango[0])
    rango[1] = int(rango[1])
    char = elem.split(" ")[1][0]
    password = elem.split(" ")[2]
    val = 0
    if (password[rango[0]-1] == char):
        val+=1
    if (password[rango[1]-1] == char):
        val+=1
    if(val == 1):
        valid += 1

print(valid)

#Out: 729
