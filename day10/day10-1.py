file = open("day10.txt")
content = file.read()
adapterJolts = content.split("\n")
adapterJolts.pop(len(adapterJolts)-1)
adapterJolts = list(map(int, adapterJolts))
adapterJolts.sort()
if adapterJolts[0] == 1:
    oneJolts =1
    threeJolts =1 #its min 1 because built-in adapter is always 3 higher than the highest adapter
else:
    oneJolts = 0
    threeJolts = 2
for i in range(len(adapterJolts)-1):
    if(adapterJolts[i+1] - adapterJolts[i] == 1):
        oneJolts+=1
    else:
        threeJolts+=1
        
print(oneJolts*threeJolts)

#Out: 2760
