def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    count = 0
    while x>1:
        if x < b:
            break
        x /= b 
        count +=1

    print(count)
    return count
myLog(61,3)