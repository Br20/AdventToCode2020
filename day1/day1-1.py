file = open("day1.txt")
content = file.read()
input = content.split("\n")
input.pop(len(input)-1)
input = list(map(int, input))
while (input != []):
    val = input.pop(0)
    if 2020-val in input:
        print(val*(2020-val))
        break
        
#Out: 1014624
