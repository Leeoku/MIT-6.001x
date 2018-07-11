'''
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened 
into [1,'a','cat',2,3,'dog',4,5] (order matters). 
'''

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(type(aList[0]))
print(aList[0])
def flatten(aList): 
    flattenedList = [] 
    for i in aList: 
        if isinstance(i,list): 
            flattenedList += flatten(i) 
        else: 
            flattenedList.append(i) 
    print(flattenedList)
    return flattenedList 

flatten(aList)