# Access each element of a string in forward and reverse orders using While loop.
str="Core Python"
#access each character using while loop
n=len(str) # n=no of chars in str
i=0
while i<n:
    print(str[i],end=' ')
    i+=1
print()  # put cursor into next line

#access each character in reverse order
i=-1
while i>=-n:
    print(str[i], end=' ')
    i-=1
print()  # put cursor into next line
#access each character in reverse order using negative index    
i=1
while i<=n:
    print(str[-i], end=' ')
    i += 1  