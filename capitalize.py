
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
