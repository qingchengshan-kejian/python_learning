#import urllib2  for python2
import urllib.request #for python3


try:
    urllib.request.urlopen("http://www.baidu.com", timeout = 2)
    print ("working connection")


except urllib.request.URLError:
    print ("No internet connection")
