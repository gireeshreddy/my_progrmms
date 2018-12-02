str1="attenting the python class on saturday"
str_to_remove = "on"
l1 = str1.split(' ')
print(l1)
strl1=" "
if (str_to_remove in l1):
    print("Found the str to remove in sentense")
    for idx in l1:
        if (idx != str_to_remove):
            strl1=strl1 + idx + " "
        else:
            break
    print(strl1)
else:
    print(str1)

