def add(a,b,*args):
    res=a+b
    for val in args:
        res +=val
    return res