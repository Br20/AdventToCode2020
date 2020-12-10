file = open("day8.txt")
content = file.read()
instructions = content.split("\n")
instructions.pop(len(instructions)-1)
instructions
for inst in range(len(instructions)-1):
    instructions[inst]=instructions[inst].split(" ")+[False]

codeLine = 0
acc = 0
while (not instructions[codeLine][2]):
    instructions[codeLine][2] = True
    if(instructions[codeLine][0] == "acc"):
        acc+= int(instructions[codeLine][1])
        codeLine+=1   
    else:
        if(instructions[codeLine][0] == "jmp"):
            codeLine+= int(instructions[codeLine][1])
        else:
            codeLine+=1
print(acc)
