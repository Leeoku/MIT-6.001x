'''
 Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. 
 The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
'''

target = 3
aDict = {1:2, 4:5, 3:2, 2:3}
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    board = []
    # Your code here  
    for key in aDict:
        if aDict[key]==target:
            board.append(key)
    return board
keysWithValue(aDict,target)