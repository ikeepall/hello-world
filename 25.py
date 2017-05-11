def a(*x,exp,base = 3):
    if exp != 5:
        result = sum(*x,exp) * base
    if exp == 5:
        result = sum(*x) * exp
    return result
    

        