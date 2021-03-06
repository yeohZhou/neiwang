import requests
import re
import sys
import threading

def getTitle(url):
    try:
	    _ = re.search('<title>(.*?)</title>', requests.get(url,timeout=20).content)  
	    print url, _.group(1)+'\n'
    except:  
        pass

def createIp(ip,port):
	tmp = []
	for x in range(255):
		tmp.append('http://'+str(ip)+'.'+str(x)+':'+str(port)+'/')
	return tmp

if __name__ == '__main__':
	ip,port = sys.argv[1:]
	urls = createIp(ip,port)
	for i in urls:
		th = threading.Thread(target = getTitle, args = (i,))
		th.start()
