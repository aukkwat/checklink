#Checklink from URL
import urllib2
import datetime

import m3u8
from bitreader import BitReader
from ts_segment import TSSegmentParser

num_segments_to_analyze_per_playlist = 1
max_frames_to_show = 30

listurl = 'http://devtab.com/services/thaitv_live/'
for link in urllib2.urlopen(listurl):
    link = link.replace('<br/>','\n')
    result=open("m3u8.txt","w")
    result.write(link)
m3u8 = open('m3u8.txt','r')
i = 0
j = 0
for bR in m3u8:
    print "-"*50
    j=j+1
    datepass = ('{:%Y-%b-%d %H:%M:%S} >>>Pass>>> '.format(datetime.datetime.now()))
    dateerror = ('{:%Y-%b-%d %H:%M:%S} >>>Error>>> '.format(datetime.datetime.now()))
    try:
        if "http://" or "https://" in bR:
            br=bR
        else:
            br="http://"+bR
        BroTher = urllib2.Request(br, headers={'User-Agent' : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT"})
        if urllib2.urlopen(BroTher).getcode() == 200 :
            i=i+1
            print "%d/%d|Ok| %s"%(i,j,br)
            result=open("normallink.txt","a")
            result.write(datepass+br)
        else:
            print "%d/%d|No| %s"%(i,j,br)
    except:
        print "%d/%d|Error| %s"%(i,j,br)
        result=open("errorlink.txt","a")
        result.write(dateerror+br)
