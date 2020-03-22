inp = input()

def isPalindrome(inp):
    inp = inp.lower()
    inp = sorted(inp)
    one = 0
    
    if(len(inp)<2):
        return True

    i = 0
    while(i< len(inp)):
        if(inp[i] == ' '):
            i += 1
            continue
        if(len(inp) > i+1 and inp[i] == inp[i+1]):
            i +=2
        else:
            one +=1
            if(one>1):
                return False
            i+=1
        
    return True

print(isPalindrome(inp))

