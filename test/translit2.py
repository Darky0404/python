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
x=translit2('Мама Мия')
print(x)
