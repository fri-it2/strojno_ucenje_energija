
# Importing required libraries
import urllib.request
from datetime import datetime
from datetime import timedelta
def time(last_start):
    """
    izvoz string datoteka v razlika v casu od 1970
    :param last_start: datum string %Y-%m-%d %H:%M:%S: %SSS
    :return: integer
    """
    year = int(last_start[0:4])
    month = int(last_start[5:7])
    day = int(last_start[8:10])
    hour = int(last_start[11:13])
    minute = int(last_start[14:16])
    second = int(last_start[17:19])
    #mili = int(last_start[21:21])
    #last_start = datetime(year, month, day, hour, minute, second, 1000 * mili)
    last_start = datetime(year, month, day, hour, minute, second)
    nov = last_start - datetime(1970, 1, 1)
    seconds = float(nov.total_seconds())
    return seconds

first_date=datetime(year, month, day, hour, minute, second)
date = datetime(2023, 1, 12, 15, 45, 0)
date=date + timedelta(minutes=15)
year=date.year
month=date.month
month= str(month).rjust(2, '0')
hour=str(date.hour).rjust(2, '0')
day=date.day
day=str(day).rjust(2, '0')

minute=date.min
minute=str(minute).rjust(2, '0')


time=str(year)+"-"+month+"-"+day+"T"+hour+":"+"minute"+":00"+"Z"
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
