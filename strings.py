#strings
name = "Tufail"
#printing indexes

print(name[0])

#str-slice

print(name[0:4])

#str-splice
print(name[2:])

print(name)
#str-reverse
print(name[::-1])
#split
print(name.split("f"))

#string concat

name2 = ("Reyaz")
print(name,  " ", name2)
print(name*3)

#Examples

sports  ="Cricket"
sports = "C" + sports[1:]
print(sports)

#Replace
sports2 = sports.replace("C", "B")
print(sports2) 
#length check
print(len(name))
#upperletter
print(name.upper())
#lowerLetter
print(name.lower())
#f string

print(f" name:{name}")