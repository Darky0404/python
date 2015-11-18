import urllib.request

urls = open('urls.txt', 'r')
frus = open('rus.txt', 'r')
feng = open('eng.txt', 'r')
rus=[]
eng=[]
seq={}
i=y=schetrus=scheteng=0
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
    for l in range(len(uurl)):
            if uurl[l] in seq.keys():
                    uurl[l] = seq[uurl[l]]



		
    outfile = open("req.htm", 'wb')
    outurl=urllib.request.urlopen('http://'+url.rstrip())
    for line in outurl.readlines():
        outfile.write(line)
        print(line)
    outurl.close()
    outfile.close()







#--------------------------------------------------------------------
##def translit2(text):
##     This method should be more easy to grasp, 
##    but throws exception:
##    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-51: ordinal not in range(128)
##    
##    symbols = string.maketrans(u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
##                               u"abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")
##    sequence = {
##        u'ж':'zh',
##        u'ц':'ts',
##        u'ч':'ch',
##        u'ш':'sh',
##        u'щ':'sch',
##        u'ю':'ju',
##        u'я':'ja',
##        u'Ж':'Zh',
##        u'Ц':'Ts',
##        u'Ч':'Ch'
##    }
##
##    for char in seq.keys():
##        text = text.replace(char, seq[char])
##
##    return text.translate(symbols)
#---------------------------------------------------------
