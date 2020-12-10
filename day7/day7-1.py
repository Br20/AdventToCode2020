file = open("day7.txt")
content = file.read()
rules = content.split("\n")
bags = {}
for rule in rules:
    if(rule == ""):
        rules.remove(rule)
    else:
        name = rule[0:rule.index("bags")-1]
        if("contain no other bags" in rule):
            bags[name] = []
        else:
            rule = rule.split("contain")[1]
            bags[name] = []
            for bag in rule.split(","):
                bagContained = bag[3:bag.index("bag")-1]
                bags.get(name).insert(0,bagContained)


withShinyGoldBags = 0
for key in bags.keys():
    toSearch = bags.get(key)
    found = False
    index = 0
    while(toSearch != [] and not found):
        if "shiny gold" in toSearch[0]:
            found = True
            withShinyGoldBags+=1
            break
        else:
            toSearch+=bags.get(toSearch[0])
            toSearch.remove(toSearch[0])
print(withShinyGoldBags)
#To realize part2, i should change a little bit structure and change all searching part 
