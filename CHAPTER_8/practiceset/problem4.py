#pattern
'''
***
**
*
'''

def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)
    
    
n = int(input("Enter the size of pattern: "))
pattern(n)