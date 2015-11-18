import urllib.request

urls = open('urls.txt', 'r')

for url in urls.readlines():
    outfile = open(url.rstrip()+".htm", 'wb')
    outurl = urllib.request.urlopen('http://'+url.rstrip())
    for line in outurl.readlines():
        outfile.write(line)
    outurl.close()
    outfile.close()
