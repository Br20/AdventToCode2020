file = open('day4.txt')
content = file.read()
passportList = content.split("\n\n")
requiredField = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
valids = 0
for passport in passportList:
    passport.replace('\n',' ')
    error = 0
    for rf in requiredField:
        try:
            passport.index(rf)
        except:
            if (rf != 'cid'):
                error+=1
    if(error == 0):
        valids+=1
print(valids)

#Out: 260
