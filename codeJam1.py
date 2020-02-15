
numberofinputs = int(input())

def clearLower(x):
    cont = True
    while(cont):
        #print "X: ", x
        smolo = x.find('o')
        smoli = x.find('i')
        if smoli<0 or smolo<0:
            cont = False
            return x
        if smoli>smolo:
            smoli = x.find('I')
        x = x[:smoli]+ x[smoli+1:smolo]+ x[smolo+1:]
        #print x



def founder(x):
    ret = 0
    cont = True
    while(cont and len(x)>0):
        #print "X: ", x
        smolo = x.find('O')
        smoli = x.find('I')
        if smoli<0 or smolo<0:
            cont = False
            return ret
        if smoli>smolo:
            cont = False
            return ret
        x = x[:smoli]+ x[smoli+1:smolo]+ x[smolo+1:]
        ret +=1
        #print x
    return ret

def main():
    arr = []
    for i in range(numberofinputs):
        inp = str(raw_input())
        arr.append(inp)
    for i in range(numberofinputs):
        print "Case #"+str(i+1)+": " +str(founder(clearLower(arr[i])))

main()



# 5
# "IiOioIoO"
# "IiOOIo"
# "IoiOiO"
# "io"
# "IIIIOOOO"


5
IiOioIoO
IiOOIo
IoiOiO
io
IIIIOOOO