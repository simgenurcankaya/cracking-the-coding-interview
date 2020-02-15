
numberofinputs = int(input())

def solve(x):
    t = ["I"]* len(x)
    for j in range(len(x)):
        if j%2 == 0:
            t[j] = 'R'
        else:
            t[j] ='L'
    return t
        

def main():
    arr = []
    for i in range(numberofinputs):
        inp = int(raw_input())
        z = []
        for j in range(inp):
            inp = str(raw_input())
            z.append(inp)
        arr += z
    print len(arr)
    print arr[0]

    for i in range(len(arr)):
        print "Case #"+str(i+1)+": " +str(solve(arr(i)))
            
main()


