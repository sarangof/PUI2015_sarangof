# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:43:29 2015

This code opens the NYC MTA api using a user key and imports json data for a given bus line. 
It imports the "real time" location of all the buses in that route. Results are printed
in console.

@author: Sara Arango-Franco.
"""
import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    print "Bus line is ", (sys.argv[2])
    print "Number of active buses is: ", len(buses)
    cont = 0
    for b in buses:
        busLat  = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        busLon  = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print 'Bus %s is in Longitude %s and Latitude %s' % (cont, busLon, busLat)
        cont +=1 