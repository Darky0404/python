import sys
f=open('a:/Coding/inpt.txt')
line=f.readline()
s=n=0
s = list(line)
while s:
    n+=1
    print(s)
f.close
print(n)
