# You a given a number N. You need to print the pattern for the given value of N.
# for N=2 the pattern will be 
# 2 2 1 1
# 2 1
# for N=3 the pattern will be 
# 3 3 3 2 2 2 1 1 1
# 3 3 2 2 1 1
# 3 2 1

# Input Format:
# The first line of input is the number of testcases T. The T test cases follow. The first line of each test case is an integer N.

# Output Format:
# For each test case, in a new line, print the required pattern in a singleline . 
# Note : Instead of printing new line print a "$" without quotes.

# Your Task:
# Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the function printPat which takes one argument 'N' denoting the length of the pattern.

# Constraints:
# 1 <= T <= 20
# 1 <= N <= 40

# Example:
# Input
# 2
# 2
# 3
# Output
# 2 2 1 1 $2 1 $
# 3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $


# Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

def printArray():
    i = 0
    while i < len(array):
        n = array[i]
        m = n
        while m > 0:
            while n >0:
                print (str(n) + " ") *m ,
                n -=1
            m -=1
            n = array[i]
            print "$",
         #   print "M = M-1" , m
        i +=1
        print "\n"
    
 
t = input()

array = []
i = 0
while i < t:
    n = input()
    array.append(n)
    i+= 1

printArray()

