import urllib

urls = open('urls.txt', 'r')

for url in urls.readlines():
    outfile = open(url.rstrip()+".htm", 'w')
    outurl=urllib.urlopen('https://geocode-maps.yandex.ru/1.x/?geocode='+url.rstrip())
    for line in outurl.readlines():
        outfile.write(line)
    outurl.close()
    outfile.close()
