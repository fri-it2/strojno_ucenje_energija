# Importing required libraries
import urllib.request

# Adding information about user agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
cas="2023-01-01T12:30:00Z"
datoteka=cas.replace(":","-")
access_token="xxx"
# setting filename and image URL
filename = 'slika2'
image_url = "https://view.eumetsat.int/geoserver/ows?service=WMS&request=GetMap&version=1.3.0&layers=msg_iodc:vis006&styles=&format=image/png&crs=EPSG:4326&bbox=13.710,45.791,14.114,45.970&width=800&height=800"+"&access_token="+access_token+"&time="+cas

filename=filename+datoteka+".png"
# calling urlretrieve function to get resource
urllib.request.urlretrieve(image_url, filename)
