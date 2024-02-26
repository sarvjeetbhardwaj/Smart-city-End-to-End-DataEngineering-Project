import os
from confluent_kafka import SerializingProducer
import simplejson

LONDON_COORDINATES = {'latitude' : 51.5074, 'longitude': -0.1278 }
BIRMINGHAM_COORDINATES = {'latitude' : 52.4862, 'longitude': -1.8904 }

## CALCULATING_MOVEMENT_INCREMENT
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['latitude'] - LONDON_COORDINATES['latitude'])/100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude'] - LONDON_COORDINATES['longitude'])/100


