import collections

file = open('day6.txt')
content = file.read()
groups = content.split("\n\n")
total = 0
for gr in groups:
    qs = gr.replace("\n",'')
    frequencies = collections.Counter(qs)
    for fr in frequencies:
        splited = gr.split("\n")
        if (splited[len(splited)-1] == ""):
            splited.remove("")
        if(frequencies[fr] == len(splited)):
            total+=1
print(total)

#3466
