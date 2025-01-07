n=3
for i in range(1, n+1):
    print(" "* (n-i), end='')
    print("*"* (2*i-1),   end=" ")
    print("")
    
n=3
for i in range(1, n+1):
    print("*"* (i), end='')
    print("")
    
n=3
for i in range(1, n+1):
    print("*"* (n), end=' ')
    print(" ")
    
n = 3
for i in range(n, 0, -1):
    print(" " * (n - i), end="")  # Print spaces for right alignment
    print("*" * i)
    
n = 3
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Print spaces for right alignment
    print("*" * i)
    
n=3
for i in range(1, n+1):
    print((n-i)*'*', end='')
    print("")