
#my solution without isSubstring method
def stringRotation(str1,str2):
    if(len(str1) != len(str2)):
        return False
    for i in range(len(str1)):
        isSub = False
        for j in range(len(str2)):
            if(str1[i] == str2[j]):
                t = str2[j]
                x = str2.replace(t,"*",1)
                isSub = True
                break;
        if(isSub == False):
            return False
    return True

    
# print(stringRotation("waterbottle","erbottlewat"))

# print(stringRotation("waterbottle","erbottlewtt"))

# print(stringRotation("simge","eSimg"))


def is_substring(string, sub):
    if sub not in string:
        return False
    return True

# this is NOT a solution lol
def stringRotation2(str1,str2):
    if(len(str1) != len(str2)):
        return False
    a = "".join(sorted(str1))
    b = "".join(sorted(str2))

    return is_substring(a,b)
    

# print(stringRotation2("waterbottle","erbottlewat"))

# print(stringRotation2("waterbottle","erbottlewtt"))

# print(stringRotation2("simge","eSimg"))


def stringRotation3(str1,str2):
    if(len(str1) != len(str2)):
        return False
    return is_substring(str1+str1,str2)

print(stringRotation3("waterbottle","erbottlewat"))

print(stringRotation3("waterbottle","erbottlewtt"))

print(stringRotation3("simge","eSimg"))

print(stringRotation3("simge","esimg"))
