#Checklink from URL
import urllib2
import datetime

import m3u8
from bitreader import BitReader
from ts_segment import TSSegmentParser

#---------------------------M3U8 Variable Start-----------------------------------------

num_segments_to_analyze_per_playlist = 1
max_frames_to_show = 30

def download_url(uri, range=None):
    print("\tDownloading {url}, Range: {range}".format(url=uri, range=range))

    opener = urllib2.build_opener(m3u8.getCookieProcessor())
    if(range is not None):
        opener.addheaders.append(('Range', range))

    response = opener.open(uri)
    content = response.read()
    response.close()

    return content

def analyze_variant(variant, bw):
    print "***** Analyzing variant ({}) *****".format(bw)
    print "\n\t** Generic information **"
    print "\tVersion: {}".format(variant.version)
    print "\tStart Media sequence: {}".format(variant.media_sequence)
    print "\tIs Live: {}".format(not variant.is_endlist)
    print "\tEncrypted: {}".format(variant.key is not None)
    print "\tNumber of segments: {}".format(len(variant.segments))

    start = 0;

    # Live
    if(not variant.is_endlist):
        if(num_segments_to_analyze_per_playlist > 3):
            start = len(variant.segments) - num_segments_to_analyze_per_playlist
        else:
            start = len(variant.segments) - 3

        if(start < 0):
            start = 0

    for i in range(start, min(start + num_segments_to_analyze_per_playlist, len(variant.segments))):
        analyze_segment(variant.segments[i], i == start)

def get_range(segment_range):
    if(segment_range is None):
        return None

    params= segment_range.split('@')
    if(params is None or len(params) != 2):
        return None

    start = int(params[1])
    length = int(params[0])

    return "bytes={}-{}".format(start, start+length-1);

def printFormatInfo(ts_parser):
    print "\n\t** Tracks and Media formats **"

    for i in range(0, ts_parser.getNumTracks()):
        track = ts_parser.getTrack(i)
        print "\tTrack #{} - Type: {}, Format: {}".format(i,
            track.payloadReader.getMimeType(), track.payloadReader.getFormat())

def printTimingInfo(ts_parser, segment):
    print "\n\t** Timing information **"
    print("\tSegment declared duration: {}".format(segment.duration))
    minDuration = 0;
    for i in range(0, ts_parser.getNumTracks()):
        track = ts_parser.getTrack(i)
        print "\tTrack #{} - Duration: {} s, First PTS: {} s, Last PTS: {} s".format(i,
            track.payloadReader.getDuration()/1000000.0, track.payloadReader.getFirstPTS() / 1000000.0,
            track.payloadReader.getLastPTS()/1000000.0)
        if(track.payloadReader.getDuration() != 0 and (minDuration == 0 or minDuration > track.payloadReader.getDuration())):
            minDuration = track.payloadReader.getDuration()

    minDuration /= 1000000.0
    print("\tDuration difference (declared vs real): {0}s ({1:.2f}%)".format(segment.duration - minDuration, abs((1 - segment.duration/minDuration)*100)))

def printFramesInfo(ts_parser):
    print "\n\t** Frames **"

    for i in range(0, ts_parser.getNumTracks()):
        track = ts_parser.getTrack(i)
        print "\tTrack #{0} - KF: {1:.03f}, Frames: ".format(i, track.payloadReader.getKeyframeInterval()/1000000.0),

        frameCount = min(max_frames_to_show, len(track.payloadReader.frames))
        for j in range(0, frameCount):
            print "{0} ".format(track.payloadReader.frames[j].type),
        print ""

def printNotes(ts_parser):
    for i in range(0, ts_parser.getNumTracks()):
        track = ts_parser.getTrack(i)
        if len(track.payloadReader.frames) > 0:
            if track.payloadReader.frames[0].type != "I":
                print "\tPlease, note track #{0} is not starting with a keyframe. This will cause not seamless bitrate switching".format(i)

def analyze_segment(segment, first_segment):
    segment_data = bytearray(download_url(segment.absolute_uri, get_range(segment.byterange)))
    ts_parser = TSSegmentParser(segment_data)
    ts_parser.prepare()

    printFormatInfo(ts_parser)

    printTimingInfo(ts_parser, segment)

    printFramesInfo(ts_parser)
    if first_segment :
        printNotes(ts_parser);

    print "\n"

#---------------------------M3U8 Variable End-----------------------------------------

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
            result=open("normallinkhls.txt","a")
            result.write(datepass+br)
        else:
            print "%d/%d|No| %s"%(i,j,br)
    except:
        print "%d/%d|Error| %s"%(i,j,br)
        result=open("errorlink.txt","a")
        result.write(dateerror+br)
