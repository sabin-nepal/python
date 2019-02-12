list_comp = [x for x in range(10)]
gen_exp = (x for x in range(10))
print("List Comprenhension>>>",list_comp)
print("Generator expression>>>",gen_exp)

for x in gen_exp:
    list_comp.append(x)

print(list_comp)

def cube(c):
    return c**3

lst = [2,3,4]

lst_n = list(map(cube,lst))
print(lst_n)

#lamda function:used for single function

list_n2 = list(map(lambda d:d**2,lst))
print(list_n2)

#filter

def isEven(n):
    if n%2==0:
        return True
    else:
        return False

num = [1,1,2,3,32,456,56534,4665,576,37]

lst = list(filter(isEven,num))

print(lst)


##prime number calculation

prime_num = [x for x in range(1,2500) if not [y for y in range(2,x) if x%y==0 ]]
print("the prime num is",prime_num)

