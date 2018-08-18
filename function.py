def times2(x):
    return x * 2

print(times2(3))

def combined_str(str1,str2):
    if(type(str1) == type("string") and type(str2) == type("str")):
        return str1 + " " + str2
    else:
        try:
            str1 = str(str1)
            str2 = str(str2)
            return str1 + " " + str2
        except:
            return "Could not be converted to strings"

print(combined_str("a", "b"))
print(combined_str(True,3.12321))
