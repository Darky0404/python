import urllib.request

urls = open('urls.txt', 'r')
frus = open('rus.txt', 'r')
feng = open('eng.txt', 'r')
rus=[]
eng=[]
seq={}
uurl=[]
kolvoadd=i=y=schetrus=scheteng=0
for line in frus:
    rus+=frus.readlines()
for lyne in feng:
    eng+=feng.readlines()
for i in eng:
    eng[scheteng]=i.strip("\n")
    scheteng+=1
for y in rus:
    rus[schetrus]=y.strip("\n")
    schetrus+=1
print(rus)
print(eng)

for url in urls.readlines():
    i=0
    kolvoadd+=1
    for i in range(len(rus)):
        be=rus[i]
        seq[rus[i]]=eng[i]
    uurl=list(url)
    raz=''
    URL=raz.join(uurl).lower()
for i in range(len(URL)):
    URL[i]
    for l in range(len(uurl)):
            if uurl[l] in seq.keys():
                    uurl[l] = seq[uurl[l]]
#URL=str(uurl).lower()
url=raz.join(uurl)
outfile = open(str(kolvoadd)+".htm", 'wb')
outurl=urllib.request.urlopen('https://geocode-maps.yandex.ru/1.x/?geocode='+url.rstrip())
for line in outurl.readlines():
    outfile.write(line)
    print(line)
outurl.close()
outfile.close()

