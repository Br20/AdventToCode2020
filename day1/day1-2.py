#How to do it in better time?. That's possible?
#Triple for? that stinks.

file = open("day1.txt")
content = file.read()
input = content.split("\n")
input.pop(len(input)-1)
input = list(map(int, input))
found = False
valA = 0
valB = 0
valC = 0
for numA in input:
    for numB in input:
        for numC in input:
            if (numA + numB + numC == 2020):
                print(numA * numB * numC)
                found = True
                break
        if (found):
            break
    if (found):
        break

#Out: 80072256
