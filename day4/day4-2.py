#ALERT: Too inefficient code. xD

import re

def checkAtt(att):
    if (att[0] == 'byr'):
        return (int(att[1]) >= 1920  and int(att[1]) <= 2002)
    if (att[0] == 'iyr'):
        return (int(att[1]) >= 2010  and int(att[1]) <= 2020)
    if (att[0] == 'eyr'):
        return (int(att[1]) >= 2020  and int(att[1]) <= 2030)
    if (att[0] == 'hgt'):
        cm = 1
        try:
            att[1].index('cm')
        except:
            cm = 0
        if (cm == 1):
            return (att[1] >= "150cm" and att[1] <= "193cm")
        else:
            return (att[1] >= "59in" and att[1] <= "76in")
    if (att[0] == 'hcl'):
        if (len(att[1]) == 7): 
            return re.match(r"#[0-9a-f]{6}", att[1])
    if (att[0] == 'ecl'):
        return re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", att[1])
    if (att[0] == 'pid'):
        if (len(att[1]) == 9):
            return re.match(r"[0-9]{9}", att[1])
    if (att[0] == 'cid'):
        return True

def checkCant(passport):
    requiredField = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    for rf in requiredField:
        try:
            passport.index(rf)
        except:
            if (rf != 'cid'):
                return False
    return True
    
file = open('day4.txt')
content = file.read()
passportList = content.split("\n\n")
valids=0
for passport in passportList:
    error = 0
    passport = passport.replace('\n',' ')
    if checkCant(passport):
        passport = passport.split(" ")
        for att in passport:
            att = att.split(":")
            if (not checkAtt(att)):
                error+=1
        if (error == 0):
            valids +=1
print(valids)
#Out: 153
