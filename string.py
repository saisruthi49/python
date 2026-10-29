# s="abcde"
# print(s[1:3])
# print(s[-3])
# print(s[:2])
# print(s[3:])
# print(s[::3])

###Looping Through Strings###

s="abcde"
for i in s:
    print(i)

###strings are immutable their values cant be changed


# s = "aBCDEF"
# # s= "A" + s[1:]
# print(s[1:])

s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABCD","abc")
print(s1)
print(s2)

