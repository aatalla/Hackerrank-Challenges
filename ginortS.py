S=raw_input()
strng=''
lst=[]
odd=[]
even=[]
capital=[]
small=[]
for i in S:
    lst.append(i)
lst.sort()
for n in lst:
    if ord(n)<=57 and ord(n)>=48:
        if ord(n)%2!=0:
            odd.append(n)
        else:
            even.append(n)
    elif ord(n)<=90 and ord(n)>=65:
        capital.append(n)
    elif ord(n)<=122 and ord(n)>=97:
        small.append(n)
odd.sort()
even.sort()
capital.sort()
small.sort()
for a in small:
    strng=strng+a
for e in capital:
    strng=strng+e
for o in odd:
    strng=strng+o
for y in even:
    strng=strng+y
print strng
