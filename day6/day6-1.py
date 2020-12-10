import collections

file = open('day6.txt')
content = file.read()
groups = content.split("\n\n")
total = 0
for qs in groups:
    qs = qs.replace("\n","")
    frequencies = collections.Counter(qs)
    total+= len(frequencies)
print(total)

#Out: 6549
