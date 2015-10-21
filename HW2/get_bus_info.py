"""
Created on Thu Sep 24 15:43:29 2015

This code opens the NYC MTA api using a user key and imports json data for a given bus line. 

It imports the "real time" location of all the buses in that route and goes over the closest
station for each bus, retrieving the stop status information (number of stops left), if available.
Results are printed in a .csv file.

@author: Sara Arango-Franco.
"""
import json
import sys
import csv
import urllib2

if __name__=='__main__':
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude','Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
        request = urllib2.urlopen(url)
        data = json.loads(request.read())
        buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
        cont = 0
        for b in buses:
            busLon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            busLat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            if 'OnwardCall' not in b['MonitoredVehicleJourney']['OnwardCalls']:
                print (busLon, busLat,"N/A","N/A")
                writer.writerow([busLat,busLon,"N/A","N/A"])
            else:
                status = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
                statName = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                writer.writerow([busLat,busLon,statName,status])