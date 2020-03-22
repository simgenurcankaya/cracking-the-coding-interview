
inp1 = input()
inp2 = input()

# o(n) ~ sort 2 strings than match

def checkPermutation(inp1,inp2):
    if(len(inp1) != len(inp2)):
        return False
    else:
        sorted1 = sorted(inp1)
        sorted2 = sorted(inp2)

        for i in range(len(inp1)):
            if(sorted1[i] != sorted2[i]):
                return False
        
        return True
 
print (checkPermutation(inp1,inp2))