
#import the Elementree Library, and set a filepath. If you know the filepath you can hardcode it like below,
#or you can open a file using the system.file.openFile() function
#once you have the filepath, parse the root of the XML tree so we can start stepping through it
import xml.etree.ElementTree as ET
filepath = "/Users/alex/Downloads/explore.gpx"#system.file.openFile()
gpxRoot = ET.parse(filepath).getroot()

#We need an array for our values, the timestamps, and quality indicators for the data we are going to import
values=[]
times = []
quality = []

#search for all of the <trk> elements
trks = gpxRoot.findall('{http://www.topografix.com/GPX/1/1}trk')
#for each <trk> elemtn, go get all of the <trkseg> elements
for trk in trks:
	trksegs = trk.findall('{http://www.topografix.com/GPX/1/1}trkseg')
	trkpts = []
	#for all of the <trkseg> elements, get the <trkpt> elements which contain the coordinate data we want
	for trkseg in trksegs:
	    trkpts = trkpts + trkseg.findall('{http://www.topografix.com/GPX/1/1}trkpt')
	    for trkpt in trkpts:
	    	#append the coordinate values to our array
	    	values.append(trkpt.get('lat'))
	    	values.append(trkpt.get('lon'))
	    	#under each <trkpt>, there is a time element for the timestamp of this value, grab that and append the values
	    	time = trkpt.find('{http://www.topografix.com/GPX/1/1}time')
	    	times.append(system.date.parse(time.text, "yyyy-MM-dd'T'HH:mm:ss"))
	    	times.append(system.date.parse(time.text, "yyyy-MM-dd'T'HH:mm:ss"))
	    	#append quality values to our quality array
	    	quality.append(192)
	    	quality.append(192)

#set out tag paths for the coordinate tags
paths = ["GPS Import/lat", "GPS Import/lon"]

#import the tags using the system.tag.storeTagHistory() function.
system.tag.storeTagHistory("Primary", "default", paths, values, quals, dates)
