
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
        if smoli<smolo:
            y = x[smoli+1:smolo]
            #print  "Y : " ,y
            smoli2 = y.find('i')
            if smoli2 >0 and smoli2+smoli < smolo: # iio
                #print "double i"
                smolo = x.find('O')
        if smoli>smolo:
            smoli = x.find('I')

        x = x[:smoli]+ x[smoli+1:smolo]+ x[smolo+1:]
        
            

        #print x
def createLower(x):
    cont = True
    ret  = ""
    while(cont ):
        y = ""
        smolo = x.find('O')
        smoli = x.find('I')
        if smoli<0 or smolo<0:
            cont = False
            ret += x
            return ret
        if smoli<smolo:
            y = x[smoli+1:smolo]
            smoli2 = y.find('I')
            if smoli2 >=0 and smoli2+smoli <= smolo: # iio
                #print "double i"
                y = y.lower()
        ret += x[:smoli+1]+ y +x[smolo]
        x = x[smolo+1:]
        
            




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
        newval  =  createLower(arr[i])
        print "Case #"+str(i+1)+": " +str(founder(clearLower(newval)))

main()




5
IiOioIoO
IIOiOo
IoiOiO
io
IiOIOIoO