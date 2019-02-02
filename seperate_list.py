list = [1,2.2,"sab",2,"bsbd",3.0]
#print(list)
intList = []
floatList = []
strlist = []

for x in list:
    if(type(x)==str):
        strlist.append(x)
    if(type(x)==int):
        intList.append(x)
    if(type(x)==float):
        floatList.append(x)

print(intList)
print(floatList)
print(strlist)
