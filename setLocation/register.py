from setLocation.auth import db
import time



def register_pothole(location):
    ref = db.reference('Pothole Data')
    new_pothole = ref.push()
    new_pothole.set(location)

def pushPotholeData(potholeClasses):
    current_time = time.localtime()

    for x in potholeClasses:
        x = int(x)
        
        potholeData = {
            'class': x,

            'Date' : {
                'day' : current_time.tm_mday,
                'month' : current_time.tm_mon ,
                'year' : current_time.tm_year
            },

            'location' : {
                'latitude' : '19.076090',
                'longitude' : '72.877426'
            }
            
            

            #'gps' : gps cordinates
            # Add any other relevant information about the pothole
        }
        register_pothole(potholeData)
   







