import unittest

def stringCompression(inp):
    retval = ""
    i = 0
    while(i< len(inp)):
        times = 0
        for j in range(i,len(inp)):
            if(inp[i] == inp[j]):
                times +=1
                if(j == len(inp) -1):
                    retval += inp[i]+ str(times)
                    i = j+1
            else:
                retval += inp[i]+ str(times)
                i = j
                break;
    
    return retval;

print(stringCompression("aabccccaaa"))  #a2b1c4a3
print(stringCompression("aaaqqweqwesdsdfpkjdfkjsdjdnnnvnvwlo")) #a3q2w1e1q1w1e1s1d1s1d1f1p1k1j1d1f1k1j1s1d1j1d1n3v1n1v1w1l1o1
print(stringCompression("aaaaajjjjjjjjjjfffffffffffnnnnnndlsssssssssssaaaaaaaappppppeeeeeeSSSSSSKKKKKKXXXXXXXMmmmmmmmssssssssm")) #a5j10f11n6d1l1s11a8p6e6S6K6X7M1m7s8m1