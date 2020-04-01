import unittest


def checker(big,smol):
    notequal = 0;
    for i in range(len(smol)):
        isAMember = False;
        for j in range(len(big)):
            if (smol[i] == big[j]):
                isAMember = True;
                break;           
        if(isAMember == False):
            notequal+=1;
    if(notequal >1):
        return False
    else:
        return True

    
def oneAway(str1,str2):
    len1 = len(str1)
    len2 = len(str2)

    if(abs(len1 - len2)>1):
        return False
    elif(len1 - len2 == 1):
        return checker(str1,str2)
    elif(len2 - len1 == 1):
        return checker(str2,str1)
    else: #equal length
        return checker(str1,str2)




class Test(unittest.TestCase):
    dataT = [("a",""),("ab","aa"),("pale","ple"),("pales","pale"),("pale","bale"),("")]
    dataF = [("aa",""),("aa","bb"),("pale","bake"),("a","abc")]

    def test_unique(self):
        # true check
        for [test_s1, test_s2] in self.dataT:
            actual = oneAway(test_s1,test_s2)
            self.assertTrue(actual)
        # false check
        for [test_s1, test_s2] in self.dataF:
            actual = oneAway(test_s1, test_s2)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()