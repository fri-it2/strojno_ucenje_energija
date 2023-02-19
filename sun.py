from pysolar.solar import *
latitude = 45.895 
log=13.906
date = datetime.datetime(2023, 2, 8, 16, tzinfo=datetime.timezone.utc)
date = datetime.datetime(2023, 2, 8, 16, tzinfo=datetime.timezone.utc)
print(get_azimuth(latitude, log, date))
print(get_altitude(latitude, log, date))
