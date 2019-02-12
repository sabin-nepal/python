import re
vaal = "I was going to the College."

if re.match('.*College.$',vaal):
    print("True")
else:
    print("False")

