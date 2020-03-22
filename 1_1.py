
inp = input()

# first solution O(N^2)  ~ recursion
def isUnique(inp):
    if(len(inp)<=1):
        return True

    for i in range(1,len(inp)):
        if (inp[0] == inp[i]):
            return False;
    return isUnique(inp[1:])     


#-----------------------------#

# second solution O(N)  ~ hash table
def isUnique2(inp):
    hash_table = [False] * 128
    if(len(inp)<=1):
        return True
    if(len(inp)>128):
        return False
    
    for i in range(len(inp)):
        if(ord(inp[i])>128):
            print ("Invalid character. Terminating. ")
            return False
        if(hash_table[ord(inp[i])]):
            return False
        else:
            hash_table[ord(inp[i])] = True
        
    return True

print (isUnique(inp))
print (isUnique2(inp))