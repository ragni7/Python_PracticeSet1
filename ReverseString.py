def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "I am learning Python"
print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse_string(s))
