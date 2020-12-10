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
    frequencies = collections.Counter(password)
    if (frequencies[char] >= rango[0] and frequencies[char] <= rango[1]):
        valid+=1
print(valid)

#Out: 582
