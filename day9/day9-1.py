file = open("day9.txt")
content = file.read()
portOutputs = content.split("\n")
def findSum(numList,sum):
    for num in numList:
        if str(sum - int(num)) in numList and sum != sum - int(num):
            return True
    return False

for indexNum in range(25,len(portOutputs)):
    if(not findSum(portOutputs[indexNum-25:indexNum],int(portOutputs[indexNum]))):
        break
print(portOutputs[indexNum])

#Out: 393911906
