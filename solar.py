# Our home location:28.5134549,77.3898596

from pysolar.solar import *
import datetime
import pytz
import math

lat = 28.5134549
long= 77.3898596


date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
r = 10
for xtime in range(6,18):
  #date = datetime.datetime.now(tz=datetime.timezone.utc)
  #print(date, get_altitude(lat,long, date),get_azimuth(lat,long, date))
  date = date.replace(hour=xtime, minute=0, second=0,microsecond=0)
  altitude = math.pi/180*get_altitude(lat,long, date)
  azimuth = math.pi/180*get_azimuth(lat,long, date)
  x = r*math.cos(altitude)*math.sin(azimuth)
  y = r*math.cos(altitude)*math.cos(azimuth)
  z = r*math.sin(altitude)
  print(date, x,y,z)
