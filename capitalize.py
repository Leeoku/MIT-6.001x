
def capitalize(txt):
    s = list(txt)
    #make everything lowercase
    for i in range(len(s)):
        if 90 >= ord(s[i]) >= 65:
            s[i] = chr(ord(s[i]) + 32)
    print(s)
    for i in range(len(s) - 1):
        print(s[i])
        #check if not symbol and next letter is not capital
        if i == 0 and 97 <= ord(s[i]) <= 122:#specific logic for first letter
            s[0] = chr(ord(s[i]) - 32)
        elif not 65 <= ord(s[i]) <= 90 and not 97 <= ord(s[i]) <= 122 and 97 <= ord(s[i+1]) <= 122:
            s[i+1] = chr(ord(s[i+1]) - 32)


            
    print("".join(s))

capitalize('@#%@$%.foo ?BAR ,bAZ')



'''
elif ord(s[i])==32 and (ord(s[i+1])>=97 and ord(s[i+1])<=122):
    s[i+1]=chr(ord(s[i+1])-32)

elif ord(i)<97 and ord(i)>122:
    #s[i] = chr(ord(i)-32)
elif ord(i)>=65 and ord(i)<=90:
    pass
    #s[i] = chr(ord(i)+32)
    
print(title('harry potter, and the chamber of secrets'))

print(title('HARRY POTTER, AND THE CHA?MBER OF SECRETS'))

print(title('@#%@$%.foo ?BAR ,bAZ'))

print(title('fo.o b.ar B.AZ')) 
'''

'''
       elif (ord(s[i])<65 and ord(s[i])>90) or (ord(s[i])<97 and ord(s[i])>122):#if not capital letter or lower letter
            if chr(ord(s[i+1]))>=65 and chr(ord(s[i+1]))<=90:
                pass
            elif chr(ord(s[i+1]))>=97 and chr(ord(s[i+1]))<=122:
                s[i+1]= chr(ord(s[i])-32)'''

''' if s[i].isalpha()==False and 97 <= ord(s[i+1])<=122:
            s[i+1]=chr(ord(s[i+1])-32)
        elif s[i].isalpha()==False and 65 <= ord(s[i+1])<=90:
            pass'''