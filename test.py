s="this is a text"
l=[]
n = []

for i in range(len(s)):
    if s[i] == ' ' or i==len(s):  
        # print(len(s))
        n.append(''.join(l))
        del l[:]
        continue
    else:
        l.append(s[i])


    
print(n[::-1])