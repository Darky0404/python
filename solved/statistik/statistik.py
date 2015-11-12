import sys
f=open('input.txt')
N=f.readlines()
s=o=[]
s4=s5=''
s4s=s5s=0
s = N[1]
o = s.strip("\n").split()
for i in o:
    I = int(i)
    if (I/2) == int(I/2):
        s4+=str(I)
        s4+=str(' ')
        s4s+=1
    else:
        s5+=str(I)
        s5+=str(' ')
        s5s+=1
with open('output.txt', 'w') as out:
    print(s5, sep=' ', file = out)
    print(s4, sep=' ', file = out)
    if s5s>s4s:
        print("NO", file = out)
    else:
        print("YES", file = out)
    
f.close()

    
