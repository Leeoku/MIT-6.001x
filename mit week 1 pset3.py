#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print: Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print: Longest substring in alphabetical order is: abc

s = 'abcdefghijklmnopqrstuvwxyz'
#make two strings equal to first char

sub = longest = s[0]

for i in range(len(s)-1): 
    if s[i+1]>=s[i]: #comparing the next char to current char
        sub +=s[i+1]
    else:
        sub=s[i+1]
    if len(sub)>len(longest):#compare longest string to current string
        longest=sub
        
print('Longest substring in alphabetical order is: {}'.format(longest))