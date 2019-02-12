f = open("file.txt","a")
f.writelines("\nthis is the file created in python")
f.close()

f12 = open("file3.txt","a")
text = input("write to the file...wrute quit to stop")

while text!='quit':
    f12.writelines(text+'\n')
    text=input()

print("done with writting now saving")
f12.close()

with open("file.txt","r") as f:
    text = f.read()
print(text)