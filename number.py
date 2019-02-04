i=0
list = []
while i<10:
    data= int(input('Enter the 10 numbers to be added in list'))
    list.append(data)
    i+=1

print(list)

#if length is unknown
#size = len(list)
#print(size)

j = 0
new_list =[]
while j <10:
    if list[j]%2==0:
        new_list.append(list[j])
    j+=1

print(new_list)

