import urllib

urls = open('urls.txt', 'r')

for url in urls.readlines():
    outfile = open(url.rstrip()+".htm", 'w')
    outurl=urllib.urlopen('http://'+url.rstrip())
    for line in outurl.readlines():
        outfile.write(line)
    outurl.close()
    outfile.close()
