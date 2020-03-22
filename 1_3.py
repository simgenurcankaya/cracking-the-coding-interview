
inp = input()
length = int(input())

# o(n)

def URLify(inp,length):
    retval  =''
    for i in range(length):
        if(inp[i] == ' '):
            retval += '%20'
            continue
        retval += inp[i]
        
    return retval


print (len(inp))
print(URLify(inp,length))