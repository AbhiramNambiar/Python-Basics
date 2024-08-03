def sd(a):
    if a==0:
        return 0
    return ((a%10)+sd(a//10))
print(sd(4205))