#Checklink from URL
import urllib2
link = 'http://52.76.39.201/m3u8.txt'
i = 0
j = 0
for bR in urllib2.urlopen(link):
    print "-"*50
    j=j+1
    try:
        if "http://" or "https://" in bR:
            br=bR
        else:
            br="http://"+bR
        BroTher = urllib2.Request(br, headers={'User-Agent' : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT"})
        if urllib2.urlopen(BroTher).getcode() == 200 :
            i=i+1
            print "%d/%d|Ok| %s"%(i,j,br)
            result=open("NormalLink.txt","a")
            result.write(br)
        else:
            print "%d/%d|No| %s"%(i,j,br)
    except:
        print "%d/%d|Error| %s"%(i,j,br)
        result=open("urlerror.txt","a")
        result.write(br)
