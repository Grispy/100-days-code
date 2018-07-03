str= input("Enter string to reverse")
s = ""
i = len(str) - 1
while i>=0:
    s = s + str[i]
    i = i - 1
print("reverse of string:-\t" + s)