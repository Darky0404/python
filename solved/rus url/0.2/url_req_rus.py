import urllib.request
kolvourl=1
def translit2(text):
    #This method should be more easy to grasp,
    #but throws exception:
    #UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-51: ordinal not in range(128)

    symbols = str.maketrans(u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
                               u"abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")
    seq = {
        u'ж':'zh',
        u'ц':'ts',
        u'ч':'ch',
        u'ш':'sh',
        u'щ':'sch',
        u'ю':'ju',
        u'я':'ja',
        u'Ж':'Zh',
        u'Ц':'Ts',
        u'Ч':'Ch'
    }

    for char in seq.keys():
        text = text.replace(char, seq[char])

    return text.translate(symbols)

urls = open('urls.txt', 'r')

for URL in urls.readlines():
    kolvourl+=1
    url = translit2(URL).strip('\n')
    outfile = open(str(kolvourl)+"url.xml", 'wb')
    outurl = urllib.request.urlopen(url.rstrip())
    for line in outurl.readlines():
        outfile.write(line)
    outurl.close()
    outfile.close()

