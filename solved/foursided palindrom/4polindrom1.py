import sys
f=open('input.txt')
s=[]
with open('output.txt', 'w') as out:
    for line in f:
        print(line)
        s = line
        if s[0] == s[3] and s[1] == s[2]:
            print('YES\n', file = out)
        else:
            print('NO\n', file = out)
f.close()

    
